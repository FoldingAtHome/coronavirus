#!/bin/env python
from openforcefield.topology import Molecule
from simtk import openmm, unit
from simtk.openmm import app
from simtk.openmm import XmlSerializer
from openmmforcefields.generators import SystemGenerator
import parmed
import time
import progressbar

#
# Global simulation parameters
#

water_model = 'tip3p'
solvent_padding = 10.0 * unit.angstroms
ionic_strength = 150 * unit.millimolar
hydrogen_mass = 4.0 * unit.amu

ffxml_filenames = ['amber14/protein.ff14SB.xml', 'amber14/tip3p.xml']

pressure = 1.0 * unit.atmospheres
temperature = 310 * unit.kelvin
collision_rate = 91.0 / unit.picoseconds
timestep = 2.0 * unit.femtoseconds
nsteps = 500 # 1 ps
niterations = 5000 # 5 ns

output_prefix = 'output/'
solvated_pdb_filename = 'solvated.pdb'
minimized_pdb_filename = 'minimized.pdb'
equilibrated_pdb_filename = 'equilibrated.pdb'

system_xml_filename = 'system.xml'
integrator_xml_filename = 'integrator.xml'
state_xml_filename = 'state.xml'

# Create protonated openforcefield Molecule from peptide inhibitor
print("Loading ligand and protonate it...")
ligand = Molecule.from_file('input/6lu7_inhibitor.pdb') # will bond by distance
# Save a copy of the fully protonated inhibitor
ligand.to_file('input/6lu7_inhibitor_protonated.sdf', file_format='sdf')
ligand.to_file('input/6lu7_inhibitor_protonated.pdb', file_format='pdb')

# Read in protein receptor
print("Loading protein...")
receptor = app.PDBFile("input/6lu7_receptor.pdb")

# Merge receptor and ligand topology and positions using ParmEd
print("Merging protein and ligand topology and positions...")
receptor_structure = parmed.load_file('input/6lu7_receptor.pdb')
ligand_structure = parmed.load_file('input/6lu7_inhibitor_protonated.pdb')
complex_structure = receptor_structure + ligand_structure

complex_topology = complex_structure.topology
complex_positions = complex_structure.positions

# Write out PDB file
with open('output/complex.pdb', 'w') as outfile:
    app.PDBFile.writeFile(complex_topology, complex_positions, outfile)

# Create system generator
print("Setting up SystemGenerator for complex...")
barostat = openmm.MonteCarloBarostat(pressure, temperature)
forcefield_kwargs = {'removeCMMotion': False, 'ewaldErrorTolerance': 1e-04, 'nonbondedMethod': app.PME, 'constraints' : app.HBonds, 
                     'hydrogenMass' : hydrogen_mass}
system_generator = SystemGenerator(forcefields=ffxml_filenames, barostat=barostat, forcefield_kwargs=forcefield_kwargs, 
                                   molecules=[ligand], 
                                   small_molecule_forcefield='gaff-2.11')

# Create the OpenMM System
print("Creating system for complex...")
system_complex = system_generator.create_system(complex_topology)

# Solvate
print('Adding solvent...')
modeller = app.Modeller(complex_topology, complex_positions)
modeller.addSolvent(system_generator.forcefield, model='tip3p', padding=10.0*unit.angstroms, ionicStrength=0.15*unit.molar)
print('System has %d atoms' % modeller.topology.getNumAtoms())

# Write initial model
print('Writing initial solvated system to %s' % solvated_pdb_filename)
with open(output_prefix + solvated_pdb_filename, 'w') as outfile:
    app.PDBFile.writeFile(modeller.topology, modeller.positions, file=outfile, keepIds=True)

# Create the system
print('Creating OpenMM System...')
system = system_generator.create_system(modeller.topology)

# Add a barostat
print('Adding barostat...')
barostat = openmm.MonteCarloBarostat(pressure, temperature)
system.addForce(barostat)

# Serialize and save the system to an xml file
print("Seralizing the system to ", output_prefix + system_xml_filename)
with open(output_prefix + system_xml_filename, 'w') as f:
    f.write(XmlSerializer.serialize(system))

# Serialize integrator
print('Creating integrator and serialize it to %s' % integrator_xml_filename)
integrator = openmm.LangevinIntegrator(temperature, collision_rate, timestep)
with open(output_prefix + integrator_xml_filename, 'w') as outfile:
    xml = openmm.XmlSerializer.serialize(integrator)
    outfile.write(xml)

# Minimize
print('Minimizing energy...')
context = openmm.Context(system, integrator)
context.setPositions(modeller.positions)
print('  initial : %8.3f kcal/mol' % (context.getState(getEnergy=True).getPotentialEnergy()/unit.kilocalories_per_mole))
openmm.LocalEnergyMinimizer.minimize(context)
print('  final   : %8.3f kcal/mol' % (context.getState(getEnergy=True).getPotentialEnergy()/unit.kilocalories_per_mole))
with open(output_prefix + minimized_pdb_filename, 'w') as outfile:
    app.PDBFile.writeFile(modeller.topology, context.getState(getPositions=True,enforcePeriodicBox=True).getPositions(), file=outfile, keepIds=True)

# Equilibrate
print('Equilibrating...')
initial_time = time.time()
for iteration in progressbar.progressbar(range(niterations)):
    integrator.step(nsteps)
elapsed_time = (time.time() - initial_time) * unit.seconds
simulation_time = niterations * nsteps * timestep
print('    Equilibration took %.3f s for %.3f ns (%8.3f ns/day)' % (elapsed_time / unit.seconds, simulation_time / unit.nanoseconds, simulation_time / elapsed_time * unit.day / unit.nanoseconds))
with open(output_prefix + equilibrated_pdb_filename, 'w') as outfile:
    app.PDBFile.writeFile(modeller.topology, context.getState(getPositions=True,enforcePeriodicBox=True).getPositions(), file=outfile, keepIds=True)
print('  final   : %8.3f kcal/mol' % (context.getState(getEnergy=True).getPotentialEnergy()/unit.kilocalories_per_mole))

# Serialize state
print('Serializing state to %s' % state_xml_filename)
state = context.getState(getPositions=True, getVelocities=True, getEnergy=True, getForces=True)
with open(output_prefix + state_xml_filename, 'w') as outfile:
    xml = openmm.XmlSerializer.serialize(state)
    outfile.write(xml)

# Serialize system
print('Serializing System to %s' % system_xml_filename)
system.setDefaultPeriodicBoxVectors(*state.getPeriodicBoxVectors())
with open(output_prefix + system_xml_filename, 'w') as outfile:
    xml = openmm.XmlSerializer.serialize(system)
    outfile.write(xml)
