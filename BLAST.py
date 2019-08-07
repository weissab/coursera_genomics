#!/c/Users/Andrea/Anaconda3/python

"""
add annotation here 


"""
import sys
import getopt

def usage():
	print""" 


BLAST.py [-h <help>] [-e <>] <filename>
-h prints this message
-
<filename> the file name to be in FASTA format
 """ 
import Bio

#BLAST sequence: blastn - search nucleotide vs nucleotide, nt is nonredundant nucleotide database all sequences NCBI has 
from Bio.Blast import NCBIWWW
Fasta_string = open("myseq.fa").read()
Results_handle = NCBIWWW.gblast("blastn", "nt", fasta_string)
 
#Reformate BLAST results for readability
from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(results_handle)

#Parsing BLAST output
len(blast_record.alighments) #gives number of alignemnts, max 50

#Set E value thereshold
E_VALUE_THRESH = 0.01
for alignment in blast_records.alignments:
	for hsp in alignments.hsps:
		if hsp.expect < E_VALUE_THRESH:
			print ('****Alignment****')
			print ('sequence:', alignment.title)
			print ('length:', alignment.length)
			print('e value:', hsp.expect)
			print(hsp.query)
			print(hsp.match)
			print (hsp.sbjct)

	