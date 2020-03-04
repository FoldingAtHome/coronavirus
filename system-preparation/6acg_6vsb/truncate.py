from simtk.openmm import app

# Load in model
pdb = app.PDBFile("input/model.pdb")
modeller = app.Modeller(pdb.topology, pdb.positions)

# Create list of chains and residues to delete
to_delete = []
for chain in modeller.topology.chains():
    if chain.id not in ['A', 'D']:
        to_delete.append(chain)
    if chain.id == 'A':
        for residue in chain.residues():
            if int(residue.id) <= 335 or int(residue.id) >= 517:
                to_delete.append(residue)

# Delete and write to file
modeller.delete(to_delete)
app.PDBFile.writeFile(modeller.topology, modeller.positions, open("input/model_truncated.pdb", "w"))