## SARS-CoV papain-like protease (PL-PRO)

### Source structures from the [protein databank](http://rcsb.org): 
* 3E9S - A new class of papain-like protease/deubiquitinase inhibitors blocks SARS virus replication (2.5 angstrom, X-ray diffraction)

### Folding@home input file preparation 
1. Remove undesired ions using pdbfixer (`clean_3e9s.py')
6. Prepare system and equilibrate using OpenMM:
    - Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with `simulate_3e9s.py`
7. Equilibrate at longer time step using OpenMM:
    - Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with `simulate_4amu_4fs.py`

Note: Did not protonate and cap this structure because we want to compare it to the structures we've automated preparation for 
from SWISS-MODEL (`system_preparation/swiss_models/`), which are not capped
