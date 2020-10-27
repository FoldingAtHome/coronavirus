# Folding@home COVID-19 efforts

This repository will contain all input files and generated datasets for the [Folding@home](https://foldingathome.org) efforts to better understand how the SARS-CoV-2 virus that causes [COVID-19](https://www.cdc.gov/coronavirus/2019-ncov/index.html) can be targeted with small molecule and antibody therapeutics.

This repository will be continuously updated to share results that are being generated on Folding@home.
You can follow along with news updates on the [Folding@home blog](https://foldingathome.org/news/) and [Folding@home twitter feed](https://twitter.com/foldingathome).

More information on this project can be found on [this Folding@home news post](https://foldingathome.org/2020/03/10/covid19-update/).

## How to contribute

You can help out by [downloading the Folding@home client](https://foldingathome.org/start-folding/) to your computer, installing it, and selecting "COVID-19" from the Web Control panel:

<img src="https://i.ibb.co/khj9b0M/image.png" width="400" />

We're especially in need of more donors with GPUs to help out, and all our GPU projects are devoted to potential drug targets for COVID-19 right now.
For more information about Folding@home, check out https://foldingathome.org

## Questions or feedback about running Folding@home

We need to keep the GitHub issue tracker clear for scientific collaborators to discuss input files and data, so please carefully route your questions or feedback as below:

* For **questions about installing or running the Folding@home client software or the science behind our projects**, please use the [Folding Forum](https://foldingforum.org/). A large community of folks can help answer your questions rapidly!
* For **bug reports with the client (with complete steps to reproduce)**, please use the [Folding@Home client issue tracker](https://github.com/FoldingAtHome/fah-issues/issues)
* For other labs working on COVID-19 targets, please use the issue tracker for [this project](https://github.com/FoldingAtHome/coronavirus/issues) to ask questions

Thanks so much for your help as we deal with the very large influx of interest!

## License

All scripts, datasets, and documentation are [permissively and openly licensed](LICENSE.md) consistent with Victoria Stodden's [Reproducible Research Standard](https://web.stanford.edu/~vcs/talks/VictoriaStoddenCommuniaJune2009-2.pdf) to ensure that they can be maximally reused, modified, and redistributed.

* All **media components** (text, figures, etc.) are licensed under the [Attribution International (CC BY) 4.0 License](https://creativecommons.org/licenses/by/4.0/)
* All **code** is licensed under the permissive open source [MIT License](https://opensource.org/licenses/MIT)
* All **datasets** are licensed under the [Creative Commons CC0 1.0 License](https://creativecommons.org/publicdomain/zero/1.0/)

## Datasets

All Folding@home simulation datasets can be found on the [MolSSI COVID-19 Molecular Structure and Therapeutics Hub](https://covid.molssi.org//org-contributions/#folding--home), created in partnership with the [Molecular Sciences Software Institute (MolSSI)](https://molssi.org).

## Participating laboratories
* [Bowman Lab (WashU)](https://bowmanlab.biochem.wustl.edu/) - Folding@home Director
* [Chodera lab (MSKCC)](https://choderalab.org)
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
* Mick Ward (Washington University in St. Louis)

# Workflow
1. Prepare input files for simulations on Folding@home (Available in `system_preparation/`)
2. Run simulations *(IN PROGRESS)*
3. Analyze simulations *(COMING SOON)*
