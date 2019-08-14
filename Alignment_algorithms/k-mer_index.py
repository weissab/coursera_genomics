#!/c/Users/Andrea/Anaconda3/python
#Input arguments: filename to get text from, pattern, k - length of the k-mer to build index library from, mismatch - number of mismatches allowed


import sys
import string
from libs.utils import read_genome


def parse_args(argv):
    filename = argv[1]
    pattern = argv[2]
    mismatch = int(argv[3])
    return filename, pattern, mismatch


"""kmer_index.py: A k-mer index for indexing a text."""

__author__ = "Ben Langmead"

import bisect


class Index(object):
    """ Holds a substring index for a text T """

    def __init__(self, t, k):
        """ Create index from all substrings of t of length k """
        self.k = 8  # k-mer length (k)
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


def approximate_match(p, t, n):
    segment_length = int(round(len(p) / (n + 1)))
    all_matches = set()
    p_idx = Index(t, segment_length)
    idx_hits = 0
    for i in range(n + 1):
        start = i * segment_length
        end = min((i + 1) * segment_length, len(p))
        matches = p_idx.query(p[start:end])

        #Extend matching to see if whole of p matches
        for m in matches:
            idx_hits += 1
            if m < start or m - start + len(p) > len(t):
                continue

            mismatches = 0

            for j in range (0, start):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
                for j in range (end, len(p)):
                    if not p[j] == t[m - start + j]:
                        mismatches += 1
                    if mismatches > n:
                        break
                if mismatches <= n:
                    all_matches.add(m - start)
    return list(all_matches), idx_hits


def main():
    filename, pattern, mismatch = parse_args(sys.argv)
    t = read_genome(filename)
    all_matches, index_hits = approximate_match(pattern, t, mismatch)
    print("there are %d exact macthes and %d index hits. Hit locations: %s" %(len(all_matches), index_hits, all_matches))

    
if __name__ == '__main__':
    main()







    """ 

    def query_index(p, t, index, mismatch): # index created from text t
        k = index.k
        offsets = set()
        hits = index.query(p)
        for h in hits: #gives back the location where the first k bases match, still have to double check the rest of p to see if it matches t
            m = 0
            match = True
            for j in range(len(p) - k):
                if p[j + k] != t[h + j + k]:
                    m += 1
                    if m > mismatch:
                        match = False
                        break
                if match:
                    offsets.add(h)
        return offsets, hits """
    

""" 
    def query_index(p, t, index): # index created from text t
        k = index.k
        matches = index.query(p)
        allmatches = set()
        for m in matches: #gives back the location where the first k bases match, still have to double check the rest of p to see if it matches t
            #verification once there is a hit
            for m in matches:
                if m < start or m - start + len(p) > len(t):
                    continue #skips rest of loop
                
                mismatch = 0
                for j in range(0, start):
                    if not p[j] == t[m-start + j]:
                        if mismatch += 1
                        if mismatches >n:
                            break
                for j in range (end, len(p)):
                    if not p[j] == t[m - start + j]:
                        mismatch += 1
                        if mismatch > n:
                            break
                if mismatch <= n:
                    all_matches.append(n - start)
        return list(all_matches) #stored as a set so that there will not be multiple entries for matching multiple matching partitions
    
       
        """