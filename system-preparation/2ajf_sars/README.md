## SARS-CoV Spike protein receptor-binding domain:ACE2

### Source structures from the [protein databank](http://rcsb.org): 
* 2AJF - SARS coronavirus spike receptor-binding domain (RBD) complexed with ACE2 (2.9 angstrom, X-ray diffraction)

### Folding@home input file preparation 
1. Extract chains A and E from 2AJF using pymol. 
2. Replace the RBD (has missing loops) in 2AJF with SWISS-MODELed SARS RBD (`2ajf_sars_rbd/input/2ajf_rbd_capped.pdb`)using Chimera:
    - Load `2ajf_rbd_capped.pdb` and 2AJF (from step 1) into Chimera. Use Tools > Structure Comparison > MatchMaker to align `2ajf_rbd_capped.pdb` to the RBD of 2AJF. Delete 2AJF RBD and save model.
3. Protonate and cap using Schrodinger's Maestro
4. Prepare system and equilibrate using OpenMM:
    - Solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with `simulate_2ajf_sars.py`
5. Equilibrate at longer time step using OpenMM:
    - Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with `simulate_4amu_4fs.py`
