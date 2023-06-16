#!/usr/bin/python

import sys, re

def main(args):
    if len(args) != 4: sys.exit("USAGE: python addSTRINGannotationsToNetwork.py annotationsOfInterest string_functional_annotations.tsv string_interactions_AllSpeckleProteinGenes.tsv > string_interactions_AllSpeckleProteinGenes_withSelectedAnnotations.txt")
    
    f = open(args[1])
    line = f.readline()[:-1]
    annotationsOfInterest = []
    while line != "":
        annotationsOfInterest.append(line.split('\t')[0])
        line = f.readline()[:-1]
    f.close()
    
    f = open(args[2])
    line = f.readline()[:-1]
    line = f.readline()[:-1]
    GOdict = {}
    while line != "":
        items = line.split("\t")
        gene = items[0]
        ID = items[3]
        description = items[4]
        if gene not in GOdict.keys():
            GOdict[gene] = ["none", "none"]
        else:
            if ID in annotationsOfInterest:
                if GOdict[gene][0] != "CL:1598": # makes sure TREX doesn't get written over
                    GOdict[gene] = [ID, description]
        line = f.readline()[:-1]
    f.close()
    
    f = open(args[3])
    line = f.readline()[:-1]
    header = line + "\tannotationID\tannotationDescription"
    print header
    line = f.readline()[:-1]
    while line != "":
        items = line.split("\t")
        gene = items[0]
        if gene not in GOdict.keys():
            print line + "\tnotSpeckle\tnotSpeckle"
        else:
            print line + "\t" + GOdict[gene][0] + "\t" + GOdict[gene][1]
        line = f.readline()[:-1]
    f.close()
    
if __name__ == "__main__": main(sys.argv)
