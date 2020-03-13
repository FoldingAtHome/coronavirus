from simtk.openmm import app
from pdbfixer import PDBFixer

fixer = PDBFixer("../structures/protease/01_raw/2z9j.pdb")

fixer.removeChains(chainIds=['B'])

fixer.removeHeterogens(keepWater=False)

app.PDBFile.writeFile(fixer.topology, fixer.positions, open("../structures/protease/01_raw/2z9j_clean.pdb", "w"))