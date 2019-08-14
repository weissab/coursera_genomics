#!/c/Users/Andrea/Anaconda3/python
#Input arguments: filename to get text from, pattern, k - length of the k-mer to build index library from, mismatch - number of mismatches allowed, interval for subsequence sampling


import sys
import bisect
from libs.utils import read_genome


def parse_args(argv):
    filename = argv[1]
    pattern = argv[2]
    mismatch = int(argv[3])
    ival = int(argv[4])
    return filename, pattern, mismatch, ival

   
class SubseqIndex(object):
    """ Holds a subsequence index for a text T """
    
    def __init__(self, t, k, ival):
        """ Create index from all subsequences consisting of k characters
            spaced ival positions apart.  E.g., SubseqIndex("ATAT", 2, 2)
            extracts ("AA", 0) and ("TT", 1). """
        self.k = 8  # num characters per subsequence extracted
        self.ival = ival  # space between them; 1=adjacent, 2=every other, etc
        self.index = []
        self.span = 1 + ival * (k - 1)
        for i in range(len(t) - self.span + 1):  # for each subseq
            self.index.append((t[i:i+self.span:ival], i))  # add (subseq, offset)
        self.index.sort()  # alphabetize by subseq
    
    def query(self, p):
        """ Return index hits for first subseq of p """
        subseq = p[:self.span:self.ival]  # query with first subseq
        i = bisect.bisect_left(self.index, (subseq, -1))  # binary search
        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != subseq:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits


def approximate_match_subseq(p, t, mismatch, ival):
    segment_length = int(round(len(p) / (mismatch+1)))
    all_matches = set()
    p_idx = SubseqIndex(t, segment_length, ival)
    idx_hits = 0
    for i in range(mismatch + 1):
        start = i
        matches = p_idx.query(p[start:])
        for m in matches:
            idx_hits += 1
            if m < start or m-start+len(p) > len(t):
                continue
            mismatches = 0
            for j in range(0, len(p)):
                if not p[j] == t[m - start + j]:
                    mismatches += 1
                    if mismatches > mismatch:
                        break
                    if mismatches <= mismatch:
                        all_matches.add(m - start)
    return list(all_matches), idx_hits


def main():
    filename, pattern, mismatch, ival = parse_args(sys.argv)
    t = read_genome(filename)
    all_matches, index_hits = approximate_match_subseq(pattern, t, mismatch, ival)
    print("there are %d exact macthes and %d index hits. Hit locations: %s" %(len(all_matches), index_hits, all_matches))


if __name__ == '__main__':
    main()
    