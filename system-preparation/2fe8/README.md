## SARS-CoV papain-like protease (PL-PRO)

### Source structures from the [protein databank](http://rcsb.org): 
* 2FE8 - SARS coronavirus papain-like protease: structure of a viral deubiquitinating enzyme (1.85 angstrom, X-ray diffraction)

### Folding@home input file preparation 
1. Remove undesired ions and chains using Pymol
2. Protonate and cap using Schrodinger's Maestro
3. Prepare system and equilibrate using OpenMM:
    - Solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with `simulate_2ef8.py`
4. Equilibrate at longer time step using OpenMM:
    - Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with `simulate_4amu_4fs.py`
