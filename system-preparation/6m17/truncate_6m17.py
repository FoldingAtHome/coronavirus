from simtk.openmm import app

pdb = app.PDBFile("../structures/01_raw/6m17.pdb")
modeller = app.Modeller(pdb.topology, pdb.positions)
to_delete = []
for chain in modeller.topology.chains():
	if chain.id not in ['B', 'E']:
		to_delete.append(chain)
	else:
		if chain.id == 'B':
			for residue in chain.residues():
				if int(residue.id) >= 610:
					to_delete.append(residue)
		for residue in chain.residues():
			if residue.name == 'NAG':
				to_delete.append(residue)
modeller.delete(to_delete)
app.PDBFile.writeFile(modeller.topology, modeller.positions, open("../structures/01_raw/6m17_truncated.pdb", "w"))