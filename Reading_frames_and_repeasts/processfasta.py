#!/c/Users/Andrea/Anaconda3/python

"""
add annotation here 
processfasta.py builds dictionary with all sequences from a fasta file
"""

import sys
import getopt

def usage():
	print""" 
processfasta.py: reads a FASTA file and builds a dictionary with all sequences bigger than a given length

processfasta.py [-h <help>] [-l <length>] <filename>
-h prints this message
-r <reading frame> reading frame for translation, 0, 1, or 2 
	(default <reading frame>=0)
<filename> the file name to be in FASTA format""" 

o, a = getopt.getopt(sys.argv[1:], 'r:h') #ignored the program name itself, l:h all arguments the user has to add with a -something, : means you have to add a value after l if you add it
#o - list of all optional arguments
#a - list of required arguments
opts = {}
seqlen = 0
for k, v in o:
	opts[k]=v
if '-h' in opts.keys():
	usage():sys.exit() #two instructions on same line seperated by :
if len(a)<1: 
	usage():sys.exit('input fasta file is missing')
if '-r' in opts.key():
	if int(opts['1']) < 0:
		print['length of sequence should be positive']: sys.exit(0)
	seqlen-opts['-l']

filename == sys.argv[1]

try: 
	f=open("myfile.fa")
except IOError:
	print("File myfile.fa does not exist")

seqs={} #initialize dictionary
for line in f:
	#lets discard  the newline at the end (if any)
	line = line.rstrip()
	#distinguish header from sequence
	if line[0]=='>': #headers always start with >. OTHEROPTION line.startswith('>')
		words=line.split() #Splits hearder based on white spaces
		name=words[0][1:] #gets rid of the> (line reads >id1 - so at position 0, characters 1 to the end)
		seq[name]= ''
	else : #sequence is not a header
		seq[name] = seqs[name] +line
close(f)

#Number of records in the file
NumRecord = len(seqs.keys())

#Length of sequences in the file
seqs_len = {}
for key in seqs.keys():
	seqs_len [key]= len(seqs[key])

#Sort dictionary of lengths
import operator
sorted_seqs_len = sorted(seqs_len.items(), key=operator.itemgetter(1))

	
	