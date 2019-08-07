#!/c/Users/Andrea/Anaconda3/python

"""
add annotation here 
DNAutil module contains a few useful functions for manipulating DNA sequences

To use: import DNAutil
Call function: DNAutil.GC(dna)
	OR

from DNAutil import * --> tells python to get all functions and definintions, or list of certain functions
then you just call function
GC(dna)

"""

def GC(dna) :
	"this function computes the GC percentage of a dna sequence"
	nbase=dna.count('n')+dna.count('N')
	gcpercent=float(dna.count('c')+dna.count('C')+dna.count('g')+dna.count('G'))*100/(len(dna-nbases))
	return gcpercent

def stop_codon(dna, frame) : #frame==0, set default value of 0 for frame
	"This function says if a DNA sequence contains an in-frame stop codon"
	stop_codon_found = Flase
	stop_codons = ['tga', 'tag', 'taa']
	for i in range (frame, len(dna), 3) : #frame allows you to select reading frame
		codon = dna[i:i+3].lower()
		if codon in stop_codons :
			stop_codon_found= True
			break
	return stop_codon_found

def reversecomplement(seq) :
	"Return the reverse complement of the dna string"
	def reverse_string(seq) :
		"returns reverse of dna string"
		return seq[::-1]
	def complement(dna) :
		"Return the complement sequence string."
	basecomplement = {'A':'T', 'a':'t', 'C':'G', 'c':'g', 'T':'A', 't':'a', 'G':'C', 'g':'c'}

	seq = reverse_string(seq)
	seq = complement(seq)
	return seq

import random

def create_dna(n, alphabet=’acgt’):
    
	return ’’.join([random.choice(alphabet) for i in range(n)])		