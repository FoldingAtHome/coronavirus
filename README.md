# coronavirus
Simulations of SARS and nCorV protein-antibody complexes

Preparation of initial structures using PyMOL manually:
* From the low resolution 6NB7 select and save the monomeric, truncated fragments of interest --> 6nb7_rbd_ab_fragment.pdb
* To the above, align 6NB8 (high ress antibody), 2AJF (high res. receptor-binding domain, with receptor), and 2GHV (high res. receptor-binding domain, apo)
* Keeping the same fragment of the antibody as in 6NB7, and all of the receptor-binding domains from 2AJF/2GHV, save two combinations: 6NB8-2AJF, and 6NB8-2GHV
* Run the resulting structures through PDBFixer (run_pdbfixer.py) to add a few atoms missing at the termini
* Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 2amu hydrogens with simulate_6nb8_2ajf.py and simulate_6nb8_2ghv.py
* Starting from the above equilibrated snapshot, equilibrate further for 1.25 ns, at 5fs timestep, 4amu hydrogens with simulate_4amu_5fs.py
* Proceed to F@h
