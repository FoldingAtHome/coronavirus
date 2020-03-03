# coronavirus
Simulations of SARS-CoV and SARS-CoV-2 protein-antibody complexes

## SARS-CoV Spike protein receptor-binding domain:S230 antibody
RCSB Structures: 
* 6NB7 - SARS-CoV complex with human neutralizing S230 antibody Fab fragment (state 2) (4.5 angstrom, Cryo-EM)
* 6NB8 - anti- SARS-CoV human neutralizing S230 antibody Fab fragment (1.5 angstrom, X-ray diffraction)
* 2AJF - SARS coronavirus spike receptor-binding domain (RBD) complexed with ACE2 (2.9 angstrom, X-ray diffraction)
* 2GHV - SARS spike protein receptor binding domain (RBD) (2.2 angstrom, X-ray diffraction)

1. Prepare initial structures using PyMOL manually:
* Extract RBD from 2GHV. 
2. Replace low resolution structures with high resolution structures using Chimera:
* Load 6NB7, 6NB8, 2GHV into Chimera. Use Tools > Structure Comparison > MatchMaker to align 2GHV to the RBD of 6NB7 and 6NB8 to the antibody of 6NB7. Delete 6NB7 stucture and save model.
3. Generate homology model using SWISS-MODEL of 2GHV SARS-CoV to SARS-CoV-2 RBD
* Used previouly extracted structure above as template sturcture and SARS-CoV-2_rbd.fasta has target sequence
4. Replace low resolution structures with high resolution structures using Chimera:
* Load 6NB7, 6NB8, 2GHV (homology modeled to SARS-CoV-2 RBD) into Chimera. Use Tools > Structure Comparison > MatchMaker to align 2GHV to the RBD of 6NB7 and 6NB8 to the antibody of 6NB7. Delete 6NB7 stucture and save model.
5. Prepare system and equilibrate using OpenMM:
* Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 2amu hydrogens with simulate_6nb8_2ghv.py
4. Equilibrate at longer time step using OpenMM:
* Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 5fs timestep, 4amu hydrogens with simulate_4amu_5fs.py
5. Run equilibrated structures on F@h

Directories:
* system_preparation/6nb8_2ghv/sars_capped
* system_preparation/6nb8_2ghv/sars-2_capped

### Uncappped structures

1. Prepare initial structures using PyMOL manually:
* From the low resolution 6NB7 select and save the monomeric, truncated fragments of interest --> 6nb7_rbd_ab_fragment.pdb
* To the above, align 6NB8 (high res. antibody), 2AJF (high res. receptor-binding domain, with receptor), and 2GHV (high res. receptor-binding domain, apo)
* Keeping the same fragment of the antibody as in 6NB7, and all of the receptor-binding domains from 2AJF/2GHV, save two combinations: 6NB8-2AJF, and 6NB8-2GHV
2. Clean structures using PDBFixer:
* Run the resulting structures through PDBFixer (run_pdbfixer.py) to add a few atoms missing at the termini
  * Note: PDBFixer did not add missing residues to 6NB8_2AJF because no SEQRES given --> ignore this structure for now 
3. Prepare system and equilibrate using OpenMM:
* Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 2amu hydrogens with simulate_6nb8_2ajf.py and simulate_6nb8_2ghv.py
4. Equilibrate at longer time step using OpenMM:
* Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 5fs timestep, 4amu hydrogens with simulate_4amu_5fs.py
5. Run equilibrated structures on F@h

Directories:
* system_preparation/6nb8_2ajf/sars_uncapped
* system_preparation/6nb8_2ghv/sars_uncapped

## SARS-CoV-2 Spike protein receptor-binding domain:ACE2
RCSB Structures: 
* 2AJF - SARS coronavirus spike receptor-binding domain (RBD) complexed with ACE2 (2.9 angstrom, X-ray diffraction)

1. Downloaded homology model of 2AJF SARS-CoV RBD to SARS-CoV-2 RBD: https://swissmodel.expasy.org/interactive/HLkhkP/models/11
2. Protonate and cap using Schrodinger's Maestro:
* Also, minimize hydrogens to remove atom clashes.
3. Prepare system and equilibrate using OpenMM:
* Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 2amu hydrogens with simulate_2ajf_sars-cov-2.py
4. Equilibrate at longer time step using OpenMM:
* Starting from the above equilibrated snapshot, equilibrate further for 1.25ns, at 5fs timestep, 4amu hydrogens with simulate_4amu_5fs.py
5. Run equilibrated structure on F@h

Directory:
* system-preparation/2ajf_sars-2

## SARS-CoV-2 main protease:peptide inhibitor
RCSB Structures: 
* 6LU7 - SARS-CoV-2 main protease in complex with an inhibitor N3

1. Rename and renumber peptide inhibitor chain using PDBFixer:
* Run 6LU7 through edit_residues.py to add rename all residues in the peptide inhibitor chain to the same residue name and id. Also rename atoms to have unique names.
2. Prepare initial structures using PyMOL manually:
* Remove waters from 6LU7
* Extract peptide inhibitor and save as separate PDB.
* Extract protease and save as separate PDB.
3. Protonate and cap the protease using Schrodinger's Maestro
4. Prepare system and equilibrate using OpenMM:
* Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 2amu hydrogens with simulate_6lu7_complex.py and simulate_6lu7_receptor.py
4. Equilibrate at longer time step using OpenMM:
* Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 5fs timestep, 4amu hydrogens with simulate_4amu_5fs.py
5. Run equilibrated structures on F@h

Directories: 
* system-preparation/6lu7_complex
* system-preparation/6lu7_receptor
