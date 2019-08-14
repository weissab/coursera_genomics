#!/c/Users/Andrea/Anaconda3/python
#Input arguments: filename to get text from, pattern, k - length of the k-mer to build index library from, m - number of mismatches


import sys
import string
from libs.utils import read_genome


def parse_args(argv):
    filename = argv[1]
    pattern = argv[2]
    kmer_len = int(argv[3])
    mismatch = int(argv[4])
    return filename, pattern, k


"""kmer_index.py: A k-mer index for indexing a text."""

__author__ = "Ben Langmead"

import bisect


class Index(object):
    """ Holds a substring index for a text T """

    def __init__(self, t, k):
        """ Create index from all substrings of t of length k """
        self.k = k  # k-mer length (k)
        self.index = []
        for i in range(len(t) - k + 1):  # for each k-mer
            self.index.append((t[i:i+k], i))  # add (k-mer, offset) pair
        self.index.sort()  # alphabetize by k-mer

    def query(self, p):
        """ Return index hits for first k-mer of p """
        kmer = p[:self.k]  # query with first k-mer
        i = bisect.bisect_left(self.index, (kmer, -1))  # binary search
        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits


def query_index(p, t, index): # index created from text t
    k = index.k
    offsets = []
    allmatches = set()
    for i in index.query(p): #gives back the location where the first k bases match, still have to double check the rest of p to see if it matches t
        #verification once there is a hit
        for m in matches:
            start = i + k
            end = i + len(p)
            if m < start or m - start + len(p) > len(t):
                continue #skips rest of loop
            
            mismatches_found = 0
            for j in range(0, start):
                if not p[j] == t[m-start + j]:
                    mismatches_found += 1
                    if mismatches_found > mismatch:
                        break
            for j in range (end, len(p)):
                if not p[j] == t[m - start + j]:
                    mismatches_found += 1
                    if mismatches_found > mismatch:
                        break

            if mismatches_found <= mismatch:
                all_matches.add(n - start)
    return list(all_matches) #stored as a set so that there will not be multiple entries for matching multiple matching partitions






     """    if p[k:] == t[i + k : i + len(p)]:
            offsets.append(i)
    return offsets """


def main():
    filename, pattern, kmer_len, mismatch = parse_args(sys.argv)
    t = read_genome(filename)
    index = Index(t, kmer_len)
    print(query_index(pattern, t, index))

if __name__ == '__main__':
    main()