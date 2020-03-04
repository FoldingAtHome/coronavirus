#!/bin/env python

import time
import progressbar
from simtk import openmm, unit
from simtk.openmm import app
from openmmtools.integrators import LangevinIntegrator

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
collision_rate = 1.0 / unit.picoseconds
timestep = 5.0 * unit.femtoseconds
splitting = 'V R O R V'
nsteps = 500 # 2.5 ps
niterations = 500 # 1.25 ns

output_prefix = 'output/'
equilibrated_pdb_filename = 'equilibrated_5fs.pdb'

system_xml_filename = 'system_5fs.xml'
integrator_xml_filename = 'integrator_5fs.xml'
state_xml_filename = 'state_5fs.xml'

system_load_xml_filename = 'system.xml'
state_load_xml_filename = 'state.xml'

# Read in the model
pdb_filename = output_prefix + 'equilibrated.pdb'
print('Loading %s' % pdb_filename)
pdb = app.PDBFile(pdb_filename)

# Load system
print('Loading OpenMM System...')
with open(output_prefix + system_load_xml_filename, 'r') as infile:
    system = openmm.XmlSerializer.deserialize(infile.read())

# Serialize integrator
print('Serializing integrator %s' % output_prefix + integrator_xml_filename)
integrator = LangevinIntegrator(temperature, collision_rate, timestep, splitting)
with open(output_prefix + integrator_xml_filename, 'w') as outfile:
    xml = openmm.XmlSerializer.serialize(integrator)
    outfile.write(xml)

print('Loading OpenMM State...')
with open(output_prefix + state_load_xml_filename, 'r') as infile:
    state = openmm.XmlSerializer.deserialize(infile.read())
context = openmm.Context(system, integrator)
context.setState(state)

# Equilibrate
print('Equilibrating...')
initial_time = time.time()
for iteration in progressbar.progressbar(range(niterations)):
    integrator.step(nsteps)
elapsed_time = (time.time() - initial_time) * unit.seconds
simulation_time = niterations * nsteps * timestep
print('    Equilibration took %.3f s for %.3f ns (%8.3f ns/day)' % (elapsed_time / unit.seconds, simulation_time / unit.nanoseconds, simulation_time / elapsed_time * unit.day / unit.nanoseconds))
with open(output_prefix + equilibrated_pdb_filename, 'w') as outfile:
    app.PDBFile.writeFile(pdb.topology, context.getState(getPositions=True,enforcePeriodicBox=True).getPositions(), file=outfile, keepIds=True)
print('  final   : %8.3f kcal/mol' % (context.getState(getEnergy=True).getPotentialEnergy()/unit.kilocalories_per_mole))

# Serialize state
print('Serializing state to %s' % output_prefix + state_xml_filename)
state = context.getState(getPositions=True, getVelocities=True, getEnergy=True, getForces=True)
with open(output_prefix + state_xml_filename, 'w') as outfile:
    xml = openmm.XmlSerializer.serialize(state)
    outfile.write(xml)

# Serialize system
print('Serializing System to %s' % output_prefix + system_xml_filename)
system.setDefaultPeriodicBoxVectors(*state.getPeriodicBoxVectors())
with open(output_prefix + system_xml_filename, 'w') as outfile:
    xml = openmm.XmlSerializer.serialize(system)
    outfile.write(xml)
