from simtk.openmm import app

pdb = app.PDBFile("../6acg_6vsb/input/model_truncated.pdb")
modeller = app.Modeller(pdb.topology, pdb.positions)
to_delete = []
for chain in modeller.topology.chains():
    if chain.id not in ['A']:
        to_delete.append(chain)
modeller.delete(to_delete)
app.PDBFile.writeFile(modeller.topology, modeller.positions, open("input/6vsb_rbd.pdb", "w"))