# Input files for simulations initiated on Folding@home

Note that these input files were rapidly prepared using available tools in order to get simulations running immediately. These files are not meant to be indicative of state-of-the-art modeling pipelines.

## Projects

SARS-CoV and SARS-CoV-2 are very similar viruses, so we are using the available structural data from both viruses (both separate simulations and homology-derived models) to aid in finding druggable sites on SARS-CoV-2 proteins, as well as, understanding why SARS-CoV-2 is fundamentally different from SARS-CoV.

Note: The directory name (located in `system_preparation`) for each structure is listed in parentheses.
Each directory contains an `input` subdirectory, containing input files for the scripts in the directory, and an `output` 
subdirectory, containing output files from the simulate scripts. The structure that is simulated on Folding@home is always `output/equilibrated_4fs.pdb`.

Apo structures:
- SARS-CoV Spike protein receptor-binding domain (`2ajf_sars_rbd`)
- SARS-CoV-2 Spike protein receptor-binding domain (`6vsb_rbd`)
- SARS-CoV main protease (3CL-PRO) (`2z9j`)
- SARS-CoV-2 main protease (3CL-PRO) (`6lu7_receptor`)
- SARS-CoV papain-like protease (PL-PRO) (`2fe8`)
- ACE2 (`2ajf_ace2` and `6m17_ace2`)
- SARS-CoV-2 NSP15 endoribonuclease HEXAMER (`6vww`)
- SARS-CoV NSP15 endoribonuclease HEXAMER (`2H85`)
- SARS-CoV-2 main protease DIMER (3CL-PRO) (`6Y2E`)
- SARS-CoV-2 main protease MONOMER (3CL-PRO) (`6Y2E`)
- SARS-CoV main protease DIMER (3CL-PRO) (`3VB3`)
- SARS-CoV-2 NSP9 DIMER (`swiss model 01 - 1qz8 homolog`) 
- SARS-CoV NSP9 DIMER (`1qz8`)
- SARS-CoV-2 NSP12 (RNA-Dependent RNA polymerase) (`swiss model 01 - 6nur homolog`)
- SARS-CoV-2 Nucleocapsid protein (N) (`6vyo`)
- SARS-CoV Nucleocapsid protein (N) (`2ofz`)
- SARS-CoV-2 NSP3 (MAC1-MAC2 domain) (`6w02`)
- SARS-CoV NSP3 (MAC1-MAC2 domain) (`2fav`)
- SARS-CoV-2 NSP10 ('6W4H')
- SARS-CoV-2 NSP13 ('swiss model 01 - 6jyt homolog')

Complex structures:
- SARS-CoV Spike protein receptor-binding domain:S230 antibody (`6nb8_2ghv_sars`)
- SARS-CoV-2 Spike protein receptor-binding domain:S230 antibody (`6nb8_2ghv_sars`)
- SARS-CoV Spike protein receptor-binding domain:ACE2 (`2ajf_sars`)
- SARS-CoV-2 Spike protein receptor-binding domain:ACE2 (`2ajf_sars-2`, `6acg_6vsb`, `6m17`)
- SARS-CoV-2 main protease:peptide-like inhibitor (`6lu7_complex`)

SWISS-MODELS: (https://swissmodel.expasy.org/repository/species/2697049)
See `swiss_models\`
