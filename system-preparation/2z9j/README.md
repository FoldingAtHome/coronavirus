## SARS-CoV main protease (3CL-PRO)

### Source structures from the [protein databank](http://rcsb.org): 
* 2Z9J - Complex structure of SARS-CoV 3C-like protease with EPDTC (1.95 angstrom, X-ray diffraction)

### Folding@home input file preparation 
1. Remove undesired ions and chains using pdbfixer (`clean_2z9j.py')
2. Prepare system and equilibrate using OpenMM:
    - Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with `simulate_2z9j.py`
3. Equilibrate at longer time step using OpenMM:
    - Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with `simulate_4amu_4fs.py`

Note: Did not protonate and cap this structure because we want to compare it to the structures we've automated preparation for 
from SWISS-MODEL (`system_preparation/swiss_models/`), which are not capped
