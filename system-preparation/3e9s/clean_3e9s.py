from pdbfixer import PDBFixer
from simtk.openmm import app

fixer = PDBFixer(pdbid="3e9s")

fixer.removeHeterogens(keepWater=False)

app.PDBFile.writeFile(fixer.topology, fixer.positions, open("../structures/protease/01_raw/3e9s_clean.pdb", "w"))