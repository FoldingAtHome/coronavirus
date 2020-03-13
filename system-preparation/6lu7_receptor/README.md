## SARS-CoV-2 main protease (3CL-PRO)

### Source structures from the [protein databank](http://rcsb.org): 
* 6LU7 - SARS-CoV-2 main protease in complex with an inhibitor N3 (2.16 angstrom, X-ray diffraction)

### Folding@home input file preparation 
1. Prepare initial structures using PyMOL manually:
    - Extract receptor (aka protease)
    - Remove waters
2. Protonate and cap the protease using Schrodinger's Maestro
3. Prepare system and equilibrate using OpenMM:
    - Solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with and `simulate_6lu7_receptor.py`
4. Equilibrate at longer time step using OpenMM:
    - Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 5fs timestep, 4amu hydrogens with `simulate_4amu_5fs.py`
5. Run equilibrated structures on F@h

