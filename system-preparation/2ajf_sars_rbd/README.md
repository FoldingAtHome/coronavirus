## SARS-CoV Spike protein receptor-binding domain

### Source structures from the [protein databank](http://rcsb.org): 
* 2AJF - SARS coronavirus spike receptor-binding domain (RBD) complexed with ACE2 (2.9 angstrom, X-ray diffraction)

### Folding@home input file preparation 
1. Prepare initial structures using PyMOL manually:
    - Extract RBD from 2AJF
2. Build in missing loops by generating homology model using SWISS-MODEL of 2AJF SARS-CoV to itself
    - Used previouly extracted structure above as template sturcture and `2ajf_rbd.fasta` as target sequence
3. Protonate and cap using Schrodinger's Maestro
4. Prepare system and equilibrate using OpenMM:
    - Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with `simulate_2ajf_sars_rbd.py`
5. Equilibrate at longer time step using OpenMM:
    - Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with `simulate_4amu_4fs.py`
