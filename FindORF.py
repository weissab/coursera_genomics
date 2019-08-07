#!/c/Users/Andrea/Anaconda3/python

#seqs = {1: 'atggtagtgatgc', 2: 'atgatgatgggatggg', 3:'ATGCCCTAG'}

import sys
import operator
from libs.utils import open_file, create_seqs, sort_seqs, pretty_print

def parse_args(argv):
    filename = argv[1]
    frame = int(argv[2]) - 1
    return filename, frame


def find_codon(frame, sequence, matches):
    for i in range (frame, len(sequence), 3) : #frame allows you to select reading rame
        codon = sequence[i:i + 3].upper()
        has_codon = codon in matches
        if has_codon:
            return i, sequence[i:]
    return None, None


def find_one_frame(frame, sequence, seqs_ORF_len, k, key):
    start_codons = ['ATG']
    stop_codons = ['TGA', 'TAG', 'TAA']
    start_index, open_sequence = find_codon(frame, sequence, start_codons)
    if start_index is not None:
        stop_index, next_chunk = find_codon(0, open_sequence, stop_codons)
        if stop_index is not None:
            if key not in seqs_ORF_len:
                seqs_ORF_len[key] = {}
            k += 1
            seqs_ORF_len[key][k] = {
                "start_index": start_index,
                "stop_index": start_index + stop_index + 3,
                "length": stop_index + 3
            }
            if len(next_chunk) >= 3:
                return find_one_frame(0, next_chunk[3:], seqs_ORF_len, k, key)


def open_reading_frame(frame, seqs):
    seqs_ORF_len = {}
    k = 0
    for key, sequence in seqs.items():
        find_one_frame(frame, sequence, seqs_ORF_len, k, key)
    return seqs_ORF_len


def main():
    filename, frame = parse_args(sys.argv)
    f = open_file(filename)
    seqs = create_seqs(f)
    f.close()
    seqs_ORF_len = open_reading_frame(frame, seqs)
    print("The tupple containing open reading frames: %s " % pretty_print(seqs_ORF_len))


if __name__ == '__main__':
    main()






