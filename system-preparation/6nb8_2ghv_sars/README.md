## SARS-CoV Spike protein receptor-binding domain:S230 antibody

### Source structures from the [protein databank](http://rcsb.org): 
* 6NB7 - SARS-CoV complex with human neutralizing S230 antibody Fab fragment (state 2) (4.5 angstrom, Cryo-EM)
* 6NB8 - anti- SARS-CoV human neutralizing S230 antibody Fab fragment (1.5 angstrom, X-ray diffraction)
* 2GHV - SARS spike protein receptor binding domain (RBD) (2.2 angstrom, X-ray diffraction)

### Folding@home input file preparation
1. Prepare initial structures using PyMOL manually:
    - Extract RBD from 2GHV, truncate 6NB7 to include only RBD and variable domain of S230 antibody, truncate 6NB8 to only include variable domain of S230 antibody.
2. Load 6NB8 into OpenMM PDBFile and write it back out to remove alternate positions.
3. Replace low resolution structures with high resolution structures using Chimera:
    - Load 6NB7, 6NB8, 2GHV into Chimera. Use Tools > Structure Comparison > MatchMaker to align 2GHV to the RBD of 6NB7 and 6NB8 to the antibody of 6NB7. Delete 6NB7 structure and save model.
4. Protonate and cap using Schrodinger's Maestro
5. Prepare system and equilibrate using OpenMM:
    - Solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with `simulate_6nb8_2ghv.py`
6. Equilibrate at longer time step using OpenMM:
7. Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with `simulate_4amu_4fs.py`
