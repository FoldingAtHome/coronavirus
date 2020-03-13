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

## Projects

SARS-CoV and SARS-CoV-2 are very similar viruses, so we are using the available structural data from SARS-CoV (both separate simulations and homology-derived models) to aid in understanding of potential SARS-CoV-2 drug targets.

Note: The directory name (located in system_preparation/) for each structure is listed in parentheses in italics

Apo structures:
- SARS-CoV Spike protein receptor-binding domain *(2ajf_sars_rbd)*
- SARS-CoV-2 Spike protein receptor-binding domain *(6vsb_rbd)*
- SARS-CoV main protease (3CL-PRO) *(2z9j)*
- SARS-CoV-2 main protease (3CL-PRO) *(6lu7_receptor)*
- SARS-CoV papain-like protease (PL-PRO) *(3e9s)*

Complex structures:
- SARS-CoV Spike protein receptor-binding domain:S230 antibody *(6nb8_2ghv_sars)*
- SARS-CoV-2 Spike protein receptor-binding domain:S230 antibody *(6nb8_2ghv_sars)*
- SARS-CoV-2 Spike protein receptor-binding domain:ACE2 *(2ajf_sars-2, 6acg_6vsb, 6m17)*
- SARS-CoV-2 main protease:peptide-like inhibitor *(6lu7_complex)*

SWISS-MODELS: (https://swissmodel.expasy.org/repository/species/2697049)
*COMING SOON*
