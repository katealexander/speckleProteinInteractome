#!/usr/bin/python

import sys, re

def main(args):
    if len(args) != 3: sys.exit("USAGE: python getSelectedSTRINGannotations.py annotationsOfInterest string_functional_annotations.tsv > selected_functional_annotations.txt")
    
    f = open(args[1])
    line = f.readline()[:-1]
    annotationsOfInterest = []
    while line != "":
        annotationsOfInterest.append(line.split('\t')[0])
        line = f.readline()[:-1]
    f.close()
    
    f = open(args[2])
    line = f.readline()[:-1]
    print line
    line = f.readline()[:-1]
    while line != "":
        items = line.split("\t")
        ID = items[3]
        if ID in annotationsOfInterest:
            print line
        line = f.readline()[:-1]
    f.close()
    
if __name__ == "__main__": main(sys.argv)
