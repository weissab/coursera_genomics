#!/c/Users/Andrea/Anaconda3/python

#find repeats - find all repeats of length n, how many times it appears and the most frquence repeat of a given length

import sys
import getopt
import operator
from libs.utils import open_file, create_seqs 


def parse_args(argv):
    filename = argv[1]
    n = int(argv[2])
    return filename, n


def find_repeats(seqs, n):
    seqs_repeat = {}
    for _, value in seqs.items():
        seq_len = len(value)
        for i in range(0, seq_len - n):
            seq_chunk = value[i:i + n]
            # seqs_repeat[seq_chunk] = seqs_repeat[seq_chunk] + 1 if seq_chunk in seqs_repeat else 1
            if seq_chunk in seqs_repeat:
                seqs_repeat[seq_chunk] += 1
            else:
                seqs_repeat[seq_chunk] = 1	
    return seqs_repeat


def main():
    filename, n = parse_args(sys.argv)
    f = open_file(filename)
    seqs = create_seqs(f)
    f.close()
    seqs_repeat = find_repeats(seqs, n)
    sorted_seqs_repeat = sorted(seqs_repeat.items(), key=operator.itemgetter(1))
    print("The tupple containing repeats and number of repeats: %s" % sorted_seqs_repeat)


if __name__ == '__main__':
    main()
    