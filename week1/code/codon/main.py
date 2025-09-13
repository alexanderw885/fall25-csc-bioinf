from dbg import DBG
from utils import read_data
import sys
import os



if __name__ == "__main__":
    argv = sys.argv

    # If input argument had a trailing '/', remove it
    path = argv[1]
    if path[-1] == '/':
        path = path[:-1]

    short1, short2, long1 = read_data('./' + path)

    k = 25
    dbg = DBG(k=k, data_list=[short1, short2, long1])
    # dbg.show_count_distribution()
    with open('./' + path + 'contig.fasta', 'w') as f:
        for i in range(20):
            c = dbg.get_longest_contig()
            if c is None:
                break
            print(i, len(c))
            f.write(f'>contig_{i}\n')
            f.write(c + '\n')
