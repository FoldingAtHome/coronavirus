## SARS-CoV-2 Spike protein receptor-binding domain:ACE2

### Source structures from the [protein databank](http://rcsb.org): 
* 6ACG - Trypsin-cleaved and low pH-treated SARS-CoV spike glycoprotein and ACE2 complex, ACE2-bound conformation 1 (5.4 angstrom, Cryo-EM)
* 6VSB - Prefusion 2019-nCoV spike glycoprotein with a single receptor-binding domain (RBD) up (3.46 angstrom, Cryo-EM)

### Folding@home input file preparation 
1. Obtain model of 6VSB superposed onto 6ACG from SWISS-MODEL
2. From this model, truncate the RBD from the spike protein using `truncate_6acg_6vsb.py`
3. Protonate and cap the protease using Schrodinger's Maestro
4. Prepare system and equilibrate using OpenMM:
    - Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with `simulate_6acg_6vsb.py`
5. Equilibrate at longer time step using OpenMM:
    - Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with `simulate_4amu_4fs.py`
