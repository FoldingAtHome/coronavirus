from simtk.openmm.app import PDBFile
from simtk.openmm.app.topology import Topology

### Rename residues and heavy atoms

## Create new topology with residues renamed

# Load topology
pdb = PDBFile("input/6lu7.pdb")
old_topology = pdb.getTopology()

# Create new topology
new_topology = Topology()
new_topology.setPeriodicBoxVectors(old_topology.getPeriodicBoxVectors())

# Copy residues and atoms to new topology and rename residues/atoms in chain C
d_old_to_new = {}
for chain in old_topology.chains():
    old_chain_id = chain.id
    new_chain = new_topology.addChain(id=old_chain_id)
    if chain.id != 'C':
        for res in chain.residues(): # Copy residues and atoms
            new_res = new_topology.addResidue(res.name, new_chain, id=res.id, insertionCode=res.insertionCode)
            for atom in res.atoms():
                new_atom = new_topology.addAtom(atom.name, atom.element, new_res)
                d_old_to_new[atom] = new_atom

    else:
        new_res = new_topology.addResidue('PEP', new_chain, id='306', insertionCode=res.insertionCode)
        for res in chain.residues(): # Copy residues and atoms
            for atom in res.atoms():
                new_atom = new_topology.addAtom(atom.name, atom.element, new_res)
                d_old_to_new[atom] = new_atom

# Copy bonds to new topology
for bond in old_topology.bonds():
    atom_1 = bond[0]
    atom_2 = bond[1]
    atom_1_new = d_old_to_new[atom_1]
    atom_2_new = d_old_to_new[atom_2]
    new_topology.addBond(atom_1_new, atom_2_new)

## Rename atom names
for residue in new_topology.residues():
    if residue.chain.id == 'C':
        atom_names = []
        atom_count = 0
        for atom in residue.atoms():
            atom_names.append(atom.name)
            atom_count += 1
        if len(set(atom_names)) == atom_count:
            # one name per atom therefore unique
            print(f'residue {residue} has unique atom names already')
        else:
            # generating new atom names
            from collections import defaultdict
            from simtk.openmm.app.element import Element
            print(f'residue {residue} does not have unique atom names. Generating now...')
            element_counts = defaultdict(int)
            for atom in residue.atoms():
                element = atom.element
                element_counts[element._symbol] += 1
                name = element._symbol + str(element_counts[element._symbol])
                atom.name = name

PDBFile.writeFile(new_topology, structure.positions, open("input/6lu7_renamed.pdb", "w"), keepIds=True)