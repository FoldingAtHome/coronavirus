from pdbfixer import PDBFixer
from simtk.openmm import app

fixer = PDBFixer("../structures/protease/01_raw/2z9j.pdb")

fixer.removeHeterogens(keepWater=False)

app.PDBFile.writeFile(fixer.topology, fixer.positions, open("../structures/protease/01_raw/3e9s_nohet.pdb", "w"))