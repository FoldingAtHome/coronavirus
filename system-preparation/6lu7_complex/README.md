## SARS-CoV-2 main protease (3CL-PRO):peptide-like inhibitor

### Source structures from the [protein databank](http://rcsb.org): 
* 6LU7 - SARS-CoV-2 main protease in complex with an inhibitor N3 (2.16 angstrom, X-ray diffraction)

### Folding@home input file preparation 
1. Rename and renumber peptide inhibitor chain using PDBFixer:
    - Run 6LU7 through edit_residues.py to add rename all residues in the peptide inhibitor chain to the same residue name and id. Also rename atoms to have unique names.
2. Prepare 6LU7 using PyMOL manually:
    - Remove waters
    - Extract peptide inhibitor and save as separate PDB.
    - Note: use `6lu7_receptor/input/6lu7_receptor.pdb` for receptor 
3. Prepare system and equilibrate using OpenMM:
    - Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with and `simulate_6lu7_complex.py`
4. Equilibrate at longer time step using OpenMM:
    - Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 5fs timestep, 4amu hydrogens with `simulate_4amu_5fs.py`

