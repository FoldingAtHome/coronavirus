# Input files for simulations initiated on Folding@home

Note that these input files were rapidly prepared using available tools in order to get simulations running immediately. These files are not meant to be indicative of state-of-the-art modeling pipelines.

## Projects

SARS-CoV and SARS-CoV-2 are very similar viruses, so we are using the available structural data from SARS-CoV (both separate simulations and homology-derived models) to aid in understanding of potential SARS-CoV-2 drug targets.

Note: The directory name (located in `system_preparation`) for each structure is listed in parentheses.
Each directory contains an `input` subdirectory, containing input files for the scripts in the directory, and an `output` 
subdirectory, containing output files from the simulate scripts. The structure that is simulated on Folding@home is always `output/equilibrated_4fs.pdb`.

Apo structures:
- SARS-CoV Spike protein receptor-binding domain (`2ajf_sars_rbd`)
- SARS-CoV-2 Spike protein receptor-binding domain (`6vsb_rbd`)
- SARS-CoV main protease (3CL-PRO) (`2z9j`)
- SARS-CoV-2 main protease (3CL-PRO) (`6lu7_receptor`)
- SARS-CoV papain-like protease (PL-PRO) (`2fe8`)

Complex structures:
- SARS-CoV Spike protein receptor-binding domain:S230 antibody (`6nb8_2ghv_sars`)
- SARS-CoV-2 Spike protein receptor-binding domain:S230 antibody (`6nb8_2ghv_sars`)
- SARS-CoV-2 Spike protein receptor-binding domain:ACE2 (`2ajf_sars-2`, `6acg_6vsb`, `6m17`)
- SARS-CoV-2 main protease:peptide-like inhibitor (`6lu7_complex`)

SWISS-MODELS: (https://swissmodel.expasy.org/repository/species/2697049)
See `swiss_models\`
