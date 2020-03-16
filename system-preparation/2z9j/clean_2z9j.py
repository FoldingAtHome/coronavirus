from simtk.openmm import app
from pdbfixer import PDBFixer

fixer = PDBFixer(pdbid="2z9j")

fixer.removeChains(chainIds=['B'])

fixer.removeHeterogens(keepWater=False)

app.PDBFile.writeFile(fixer.topology, fixer.positions, open("input/2z9j_clean.pdb", "w"))