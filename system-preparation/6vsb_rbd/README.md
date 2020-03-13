## SARS-CoV-2 Spike protein receptor-binding domain

### Source structures from the [protein databank](http://rcsb.org): 
* 6VSB - Prefusion 2019-nCoV spike glycoprotein with a single receptor-binding domain (RBD) up (3.46 angstrom, Cryo-EM)

### Folding@home input file preparation
1. Extract RBD from `6acg_6vsb/input/model_truncated.pdb` using `keep_rbd.py`
2. Protonate and cap using Schrodinger's Maestro
3. Prepare system and equilibrate using OpenMM:
* Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with `simulate_2ajf_sars-2.py`
4. Equilibrate at longer time step using OpenMM:
* Starting from the above equilibrated snapshot, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with `simulate_4amu_4fs.py`
