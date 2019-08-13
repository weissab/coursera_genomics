#!/c/Users/Andrea/Anaconda3/python


import sys
from libs.utils import reverse_complement, read_genome


# import file from website with ipython
# !wget --no-check http:// ... 

# if the pattern is not an inputed sequence from user but a file of reads
# pattern, _ = readFastq('FILENAME_READS')


def parse_args(argv):
    filename = argv[1]
    pattern = argv[2]
    return filename, pattern


def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences



def main():
    filename, pattern = parse_args(sys.argv)
    reference_genome = read_genome(filename)
    #f.close() opened in utils, should I close it in utils?????
    result = naive(pattern, reference_genome)
    print(" The pattern matches the genome %d times at locations %s " % (len(result), result))

if __name__ == '__main__':
    main()