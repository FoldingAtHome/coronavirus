## SARS-CoV ACE2

### Source structures from the [protein databank](http://rcsb.org): 
* 2AJF - SARS coronavirus spike receptor-binding domain (RBD) complexed with ACE2 (2.9 angstrom, X-ray diffraction)

### Folding@home input file preparation 
1. Extract ACE2 chain from 2AJF.
2. Protonate and cap using Schrodinger's Maestro
3. Prepare system and equilibrate using OpenMM:
    - Solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with `simulate_2ajf_ace2.py`
4. Equilibrate at longer time step using OpenMM:
    - Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with `simulate_4amu_4fs.py`
