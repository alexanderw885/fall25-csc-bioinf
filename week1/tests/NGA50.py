import sys
import os
import numpy as np

if __name__ == "__main__":
    argv = sys.argv
    test = open('./' + argv[1] + "/contig.fasta", 'r')
    lengths = []
    for line in test:
        if line[0] == '>':
            continue
        line.strip()
        lengths.append(len(line))

    sum = (np.sum(lengths))

    print("NOT CURRENTLY CALCULATING THE NGA50: CURRENTLY JUST N50")
    nga = 0
    for x in lengths:
        if x < sum:
            nga = x
            break
        sum = sum - x

    print(nga)
    
    