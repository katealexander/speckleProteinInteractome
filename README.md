# Speckle Protein Interactome
This repository describes how I used protein protein interactome data of speckle protein genes to gain insights into the functional categories and complexes of speckle-resident proteins. 

# Requirements and software
Python 2.7

R - see below for R session info

[Cytoscape](https://apps.cytoscape.org/apps/stringapp)

# Speckle Protein Network
To get a network of speckle-resident proteins and relevant functional complexes, I used [StringDB](https://string-db.org/) with speckle-resident proteins from the [Human Protein Atlas](https://www.proteinatlas.org/about/download) as input.

I applied the following filters in StringDB:
- Physical subnetwork
- High confidence
- Experiments and datasets
- 200 interactors in first shell
- 100 interactors in second shell

I downloaded the above network, called "string_interactions_AllSpeckleProteinGenes.tsv", as well as significant STRING neighborhood annotations, called "enrichment.NetworkNeighborAL.tsv"

# Make a boxplot of functional annotation expression
### Extracting the functional annotations of interest:
```python getSelectedSTRINGannotations.py annotationsOfInterest string_functional_annotations.tsv > selected_functional_annotations.txt```

### Adding the speckle signature ratio
```python addSignatureRatio.py medianGeneExpression_KIRC_specklepatientGroups.txt selected_functional_annotations.txt > selected_functional_annotations_withKIRCratios.txt```

### Making the boxplot
```Rscript boxplotForGOterms.R```

The above script will also output t test statistics for whether the GO categories have a log2 ratio gene expression different than 0.

# Add annotations of interest to network
Using the annotations file ("annotationsOfInterest"), I added functional annotations to the network so it can be viewed in cytoscape with annotations of different colors. Not that here only one annotation is set per protein, so it's important to have mostly non-overlapping functional categories.

```python addSTRINGannotationsToNetwork.py annotationsOfInterest string_functional_annotations.tsv string_interactions_AllSpeckleProteinGenes.tsv > string_interactions_AllSpeckleProteinGenes_withSelectedAnnotations.txt```

The above script outputs the file, "string_interactions_AllSpeckleProteinGenes_withSelectedAnnotations.txt", which can be loaded into cytoscape.

Within cytoscape, I set the colors for the annotations and saved the network, "coloredNetwork.cys", and image, "string_interactions_AllSpeckleProteinGenes_withSelectedAnnotations.png" 


