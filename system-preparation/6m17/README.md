## SARS-CoV-2 Spike protein receptor-binding domain:ACE2

### Source structures from the [protein databank](http://rcsb.org): 
* 6M17 - The 2019-nCoV RBD/ACE2-B0AT1 complex (2.9 angstrom, Cryo-EM)

### Folding@home input file preparation 
1. Truncate ACE2 and extract truncated ACE2, RBD from `6M17.pdb` using `truncate_6m17.pdb`
2. Protonate and cap using Schrodinger's Maestro
3. Prepare system and equilibrate using OpenMM:
    - Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with `simulate_6m17.py`
4. Equilibrate at longer time step using OpenMM:
    - Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with `simulate_4amu_4fs.py`
