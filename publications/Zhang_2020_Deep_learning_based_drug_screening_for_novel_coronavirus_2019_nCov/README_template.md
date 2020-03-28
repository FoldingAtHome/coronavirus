# **Citation**
 Zhang, Haiping, et al. "Deep learning based drug screening for novel coronavirus 2019-nCov." (2020).

# **Summary of Article**
* Built a homology model of the main protease structure (there is now an experimental structure for this), focus on the known active site.
* Using deep learning method DFCNN (densely fully connected neural network) to identify and rank the protein-ligand interactions. 
* Model is trained on data from PDBBIND. 
* CFCNN runs fast as no docking or MD is needed
* Screening with 4 chemical compound databases and all tripeptides.
	* chemdiv
	* Targetmol: Approved drugs, Natural compound and bioactive compound set.
	* Exhaustive tri-peptide library
* Of the tripeptides: I, K and P seem to have high probability of binding
