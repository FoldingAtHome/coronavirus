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
timestep = 4.0 * unit.femtoseconds
splitting = 'V R O R V'
nsteps = 500 # 2.5 ps
niterations = 500 # 1.25 ns

output_prefix = 'output/'
equilibrated_pdb_filename = 'equilibrated_4fs.pdb'

system_xml_filename = 'system_4fs.xml'
integrator_xml_filename = 'integrator_4fs.xml'
state_xml_filename = 'state_4fs.xml'

system_load_xml_filename = 'system.xml'
state_load_xml_filename = 'state.xml'


def serialize(filename, data):
    with open(os.path.join(output_prefix, filename), 'w') as outfile:
        xml = openmm.XmlSerializer.serialize(data)
        outfile.write(xml)


def deserialize(filename):
    with open(os.path.join(output_prefix, filename), 'r') as infile:
        return openmm.XmlSerializer.deserialize(infile.read())


# Read in the model
pdb_filename = output_prefix + 'equilibrated.pdb'
print('Loading %s' % pdb_filename)
pdb = app.PDBFile(pdb_filename)

print('Loading OpenMM System...')
system = deserialize(system_load_xml_filename)

# Serialize integrator
print('Serializing integrator %s' % output_prefix + integrator_xml_filename)
integrator = LangevinIntegrator(temperature, collision_rate, timestep, splitting)
serialize(integrator_xml_filename, integrator)

print('Loading OpenMM State...')
state = deserialize(state_load_xml_filename)
context = openmm.Context(system, integrator)
context.setState(state)

# Equilibrate
print('Equilibrating...')
initial_time = time.time()
for iteration in progressbar.progressbar(range(niterations)):
    integrator.step(nsteps)
elapsed_time = (time.time() - initial_time) * unit.seconds
simulation_time = niterations * nsteps * timestep
print('    Equilibration took %.3f s for %.3f ns (%8.3f ns/day)' % (
    elapsed_time / unit.seconds,
    simulation_time / unit.nanoseconds,
    simulation_time / elapsed_time * unit.day / unit.nanoseconds)
)

with open(output_prefix + equilibrated_pdb_filename, 'w') as outfile:
    app.PDBFile.writeFile(
        pdb.topology,
        context.getState(getPositions=True, enforcePeriodicBox=True).getPositions(),
        file=outfile,
        keepIds=True)

print('  final   : %8.3f kcal/mol' % (
    context.getState(getEnergy=True).getPotentialEnergy()/unit.kilocalories_per_mole))

# Serialize state
print('Serializing state to %s' % output_prefix + state_xml_filename)
state = context.getState(getPositions=True, getVelocities=True, getEnergy=True, getForces=True)
serialize(state_xml_filename, state)

# Serialize system
print('Serializing System to %s' % output_prefix + system_xml_filename)
system.setDefaultPeriodicBoxVectors(*state.getPeriodicBoxVectors())
serialize(system_xml_filename, system)
