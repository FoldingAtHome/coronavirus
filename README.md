# Folding@home COVID-19 efforts

This repository will contain all input files and generated datasets for the [Folding@home](http://foldingathome.org) efforts to better understand how the SARS-CoV-2 virus that causes [COVID-19](https://www.cdc.gov/coronavirus/2019-ncov/index.html) can be targeted with small molecule and antibody therapeutics.

This repository will be continuously updated to share results that are being generated on Folding@home.
You can follow along with news updates on the [Folding@home blog](https://foldingathome.org/news/) and [Folding@home twitter feed](https://twitter.com/foldingathome).

More information on this project can be found on [this Folding@home news post](https://foldingathome.org/2020/03/10/covid19-update/).

## Datasets

Links to Folding@home generated datasets will be posted here as soon as the incoming data is batch-processed.

## Participating laboratories
* [Bowman Lab (WashU)](https://bowmanlab.biochem.wustl.edu/) - Folding@home Director
* [Chodera lab (MSKCC)](http://choderalab.org)
* [Voelz lab (Temple)](http://www.voelzlab.org/)

## How to contact / collaborate with us
* Reach out to Folding@home Director [Dr. Greg Bowman](https://bowmanlab.biochem.wustl.edu/) via [email](mailto:g.bowman@wustl.edu) or [twitter](https://twitter.com/drGregBowman)

## Collaborators
* [DiamondMX](https://www.diamond.ac.uk/Instruments/Mx/Fragment-Screening.html) has carried out a fragment screen against the SARS-CoV-2 main viral protease that has generated [many new X-ray structures with small molecules bound](https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem.html) posted openly to advance the development of tool compounds and potential small molecule therapeutics. They are actively looking for funds for purchasing new compounds to screen to elaborate on these initial hits.

## Contributors

* John Chodera (Memorial Sloan Kettering Cancer Center)
* Matthew Hurley (Temple University)
* Vincent Voelz (Temple University)
* [Rafal Wiewiora](https://www.mskcc.org/research/ski/labs/members/rafal-wiewiora) (Tri-Institutional Graduate Program in Chemical Biology)
* Ivy Zhang (Computational Biology and Medicine Graduate Program)

# Input files for simulations initiated on Folding@home

Note that these input files were rapidly prepared using available tools in order to get simulations running immediately. These files are not meant to be indicative of state-of-the-art modeling pipelines.

## SARS-CoV and SARS-CoV-2 Spike protein receptor-binding domain:S230 antibody

SARS-CoV and SARS-CoV-2 are very similar viruses, so we are using the avilable structural data from SARS-CoV (both separate simulations and homology-derived models) to aid in understanding of potential SARS-CoV-2 drug targets.

### Source structures from the [protein databank](http://rcsb.org): 
* 6NB7 - SARS-CoV complex with human neutralizing S230 antibody Fab fragment (state 2) (4.5 angstrom, Cryo-EM)
* 6NB8 - anti- SARS-CoV human neutralizing S230 antibody Fab fragment (1.5 angstrom, X-ray diffraction)
* 2AJF - SARS coronavirus spike receptor-binding domain (RBD) complexed with ACE2 (2.9 angstrom, X-ray diffraction)
* 2GHV - SARS spike protein receptor binding domain (RBD) (2.2 angstrom, X-ray diffraction)

### Capped structures
1. Prepare initial structures using PyMOL manually:
* Extract RBD from 2GHV, truncate 6NB7 to include only RBD and variable domain of S230 antibody, truncate 6NB8 to only include variable domain of S230 antibody.
2. Replace low resolution structures with high resolution structures using Chimera:
* Load 6NB7, 6NB8, 2GHV into Chimera. Use Tools > Structure Comparison > MatchMaker to align 2GHV to the RBD of 6NB7 and 6NB8 to the antibody of 6NB7. Delete 6NB7 stucture and save model.
3. Generate homology model using SWISS-MODEL of 2GHV SARS-CoV to SARS-CoV-2 RBD
* Used previouly extracted structure above as template sturcture and SARS-CoV-2_rbd.fasta has target sequence
4. Replace low resolution structures with high resolution structures using Chimera:
* Load 6NB7, 6NB8, 2GHV (homology modeled to SARS-CoV-2 RBD) into Chimera. Use Tools > Structure Comparison > MatchMaker to align 2GHV to the RBD of 6NB7 and 6NB8 to the antibody of 6NB7. Delete 6NB7 stucture and save model.
5. Prepare system and equilibrate using OpenMM:
* Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with simulate_6nb8_2ghv.py
6. Equilibrate at longer time step using OpenMM:
* Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with simulate_4amu_4fs.py
7. Run equilibrated structures on F@h

Directories:
* system_preparation/6nb8_2ghv/sars_capped/
* system_preparation/6nb8_2ghv/sars-2_capped/

### Uncapped structures

1. Prepare initial structures using PyMOL manually:
* From the low resolution 6NB7 select and save the monomeric, truncated fragments of interest --> 6nb7_rbd_ab_fragment.pdb
* To the above, align 6NB8 (high res. antibody), 2AJF (high res. receptor-binding domain, with receptor), and 2GHV (high res. receptor-binding domain, apo)
* Keeping the same fragment of the antibody as in 6NB7, and all of the receptor-binding domains from 2AJF/2GHV, save two combinations: 6NB8-2AJF, and 6NB8-2GHV
2. Clean structures using PDBFixer:
* Run the resulting structures through PDBFixer (run_pdbfixer.py) to add a few atoms missing at the termini
  * Note: PDBFixer did not add missing residues to 6NB8_2AJF because no SEQRES given --> ignore this structure for now 
3. Prepare system and equilibrate using OpenMM:
* Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with simulate_6nb8_2ajf.py and simulate_6nb8_2ghv.py
4. Equilibrate at longer time step using OpenMM:
* Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with simulate_4amu_4fs.py
5. Run equilibrated structures on F@h

Directories:
* system_preparation/6nb8_2ajf/sars_uncapped/
* system_preparation/6nb8_2ghv/sars_uncapped/
Note: we did not prepare SARS-CoV-2 using this approach. See capped structure for SARS-CoV-2 RBD:S230 Antibody

## SARS-CoV-2 Spike protein receptor-binding domain:ACE2

### Using homology model of SARS-CoV to SARS-CoV-2 RBD
RCSB Structures: 
* 2AJF - SARS coronavirus spike receptor-binding domain (RBD) complexed with ACE2 (2.9 angstrom, X-ray diffraction)

1. Download homology model of 2AJF SARS-CoV RBD to SARS-CoV-2 RBD: https://swissmodel.expasy.org/interactive/HLkhkP/models/11
2. Protonate and cap using Schrodinger's Maestro:
* Also, minimize hydrogens to remove atom clashes.
3. Prepare system and equilibrate using OpenMM:
* Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with simulate_2ajf_sars-2.py
4. Equilibrate at longer time step using OpenMM:
* Starting from the above equilibrated snapshot, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with simulate_4amu_4fs.py
5. Run equilibrated structure on F@h

Directory:
* system-preparation/2ajf_sars-2/

### Using Cryo-EM structure of SARS-CoV-2 RBD
RCSB Structures: 
* 6ACG - Trypsin-cleaved and low pH-treated SARS-CoV spike glycoprotein and ACE2 complex, ACE2-bound conformation 1 (5.4 angstrom, Cryo-EM)
* 6VSB - Prefusion 2019-nCoV spike glycoprotein with a single receptor-binding domain (RBD) up (3.46 angstrom, Cryo-EM)

0. Obtain model of 6VSB superposed onto 6ACG from SWISS-MODEL
1. From this model, truncate the RBD from the spike protein:
* Run model through truncate.py
2. Protonate and cap the protease using Schrodinger's Maestro
3. Prepare system and equilibrate using OpenMM:
* Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with simulate_6acg_6vsb.py
4. Equilibrate at longer time step using OpenMM:
* Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 4fs timestep, 4amu hydrogens with simulate_4amu_4fs.py
5. Run equilibrated structures on F@h

Directories: 
* system-preparation/6acg_6vsb/


## SARS-CoV-2 main protease:peptide inhibitor
RCSB Structures: 
* 6LU7 - SARS-CoV-2 main protease in complex with an inhibitor N3

1. Rename and renumber peptide inhibitor chain using PDBFixer:
* Run 6LU7 through edit_residues.py to add rename all residues in the peptide inhibitor chain to the same residue name and id. Also rename atoms to have unique names.
2. Prepare initial structures using PyMOL manually:
* Remove waters from 6LU7
* Extract peptide inhibitor and save as separate PDB.
* Extract protease and save as separate PDB.
3. Protonate and cap the protease using Schrodinger's Maestro
4. Prepare system and equilibrate using OpenMM:
* Add hydrogens, solvate, minimize, and equilibrate for 5ns, at 2fs timestep, 4amu hydrogens with simulate_6lu7_complex.py and simulate_6lu7_receptor.py
5. Equilibrate at longer time step using OpenMM:
* Starting from the above equilibrated snapshots, equilibrate further for 1.25ns, at 5fs timestep, 4amu hydrogens with simulate_4amu_5fs.py
6. Run equilibrated structures on F@h

Directories: 
* system-preparation/6lu7_complex/
* system-preparation/6lu7_receptor/
