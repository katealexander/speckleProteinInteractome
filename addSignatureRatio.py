#!/usr/bin/python

import sys, re, math

def main(args):
    if len(args) != 3: sys.exit("USAGE: python addSignatureRatio.py medianGeneExpression_KIRC_specklepatientGroups.txt selected_functional_annotations.txt > selected_functional_annotations_withKIRCratios.txt")
    
    f = open(args[1])
    line = f.readline()[:-1]
    line = f.readline()[:-1]
    ratioDict = {}
    while line != "":
        items = line.split()
        gene = items[1]
        ratio = math.log(float(items[2])/float(items[4]), 2)
        ratioDict[gene] = ratio
        line = f.readline()[:-1]
    f.close()
    
    f = open(args[2])
    line = f.readline()[1:-1]
    header = line + "\tSignatureRatioKIRC\tAbbreviation"
    print header
    line = f.readline()[:-1]
    while line != "":
        items = line.split("\t")
        gene = items[0]
        GO = items[3]
        if GO == "CL:1598" :
            a = "1_TREX"
        elif GO == "GO:1903311":
            a = "2_RNAmetabolism"
        elif GO == "GO:0071007":
            a = "3_U2cat"
        elif GO == "GO:0071006":
            a = "3_U2cat"
        elif GO == "GO:0071005":
            a = "4_U2precat"
        elif GO == "GO:0006281":
            a = "5_DNArepair"
        elif GO == "GO:0006325":
            a = "6_chromatin"
        elif GO == "GO:0006366":
            a = "7_pretranscriptionAndElongation"

        
        if gene in ratioDict.keys():
            print line + "\t" + str(ratioDict[gene]) + "\t" + a
        else:
            print line + "\t0\t" + a
        line = f.readline()[:-1]
    f.close()

if __name__ == "__main__": main(sys.argv)
