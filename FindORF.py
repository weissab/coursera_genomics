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


#def open_reading_frames(frame, seqs):
    #"This function says if a DNA sequence contains an in-frame stop codon"


def open_reading_frame(frame, seqs, seqs_ORF_len, k):
    start_codons = ['ATG']
    stop_codons = ['TGA', 'TAG', 'TAA']
    for key, sequence in seqs.items():
        start_index, open_sequence = find_codon(frame, sequence, start_codons)
        if start_index is not None:
            stop_index, next_chunk = find_codon(0, open_sequence, stop_codons)
            if stop_index is not None:
                # finale_squence = open_sequence[:stop_index + 3]
                if key not in seqs_ORF_len:
                    seqs_ORF_len[key] = {}
                    k += 1
                    seqs_ORF_len[key][k] = {
                    "start_index": start_index,
                    "stop_index": start_index + stop_index + 3,
                    "length": stop_index + 3
                    }
            return next_chunk, seqs_ORF_len, k
        if len(next_chunk) > 0:
            next_chunk, seqs_ORF_len, k = open_reading_frame(0, next_chunk, seqs_ORF_len, k)
        # if len of sequence is smaller than stop index, start looking for codon start again 
    return seqs_ORF_len


def main():
    filename, frame = parse_args(sys.argv)
    f = open_file(filename)
    seqs = create_seqs(f)
    f.close()
    seqs_ORF_len = {}
    k = 0
    seqs_ORF_len = open_reading_frame(frame, seqs, seqs_ORF_len, k)
    print("The tupple containing open reading frames: %s " % pretty_print(seqs_ORF_len))


if __name__ == '__main__':
    main()






