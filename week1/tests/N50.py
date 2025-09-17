import sys
import os
import numpy as np

if __name__ == "__main__":
    test = open("./week1/data/data1/contig.fasta", 'r')
    lengths = []
    for line in test:
        if line[0] == '>':
            continue
        line.strip()
        lengths.append(len(line))

    sum = (np.sum(lengths)) / 2
    print(sum)

    n50 = 0
    for x in lengths[::-1]:
        print(str(sum) + "   " + str(x))
        if x >= sum:
            n50 = x
            break
        sum = sum - x

    print(n50)
    
    