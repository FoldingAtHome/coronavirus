import pdbfixer
from simtk.openmm.app import PDBFile

fixer = pdbfixer.PDBFixer('6nb8_2ajf_complex.pdb')
fixer.findMissingResidues()
fixer.findMissingAtoms()
fixer.addMissingAtoms()
PDBFile.writeFile(fixer.topology, fixer.positions, open('6nb8_2ajf_complex_fixed.pdb', 'w'))
