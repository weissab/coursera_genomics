#!/c/Users/Andrea/Anaconda3/python


import sys
import operator
from libs.utils import reverse_complement, read_genome


# import file from website with ipython
# !wget --no-check http:// ... 

# if the pattern is not an inputed sequence from user but a file of reads
# pattern, _ = readFastq('FILENAME_READS')


def parse_args(argv):
    filename = argv[1]
    pattern = argv[2]
    mismatch = int(argv[3]) # number of max mismatches allowed
    return filename, pattern, mismatch


def naive(p, t, mismatch):
    occurrences = [] 
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        k = 0
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                k += 1
                if k >= mismatch:
                    match = False
                    break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences


def main():
    filename, pattern, mismatch = parse_args(sys.argv)
    reference_genome = read_genome(filename)
    #f.close() opened in utils, should I close it in utils?????
    result = naive(pattern, reference_genome, mismatch)
    print(" The pattern matches the genome %d times at locations %s " % (len(result), result))
    #print(" The pattern matches the genome %d times " % len(result))
if __name__ == '__main__':
    main()