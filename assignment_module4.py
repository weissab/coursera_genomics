#!/c/Users/Andrea/Anaconda3/python

import sys
import getopt

def usage():
	print("""processfasta.py: reads a FASTA file and builds a dictionary with all sequences bigger than a given length
processfasta.py [-h] [-l <length>] <filename>
#optional arguments have square brackets
-h prints this message
-r <reading frame> reading frame for translation, 0, 1, or 2 
	(default <reading frame>=0)
<filename> the file name to be in FASTA format""")


o, a = getopt.getopt(sys.argv[1:], 'r:h') 
#ignored the program name itself
#l:h all arguments the user has to add with a -something, 
# (:) means you have to add a value after l if you add it ex: -l 250
#o - list of all optional arguments
#a - list of required arguments
opts = {} #make a dictionary of arguments with the value
seqlen = 0
for k, v in o:
	opts[k]=v #give the value for each argument
if '-h' in opts.keys():
	usage();sys.exit() #two instructions on same line seperated by ;
if len(a)<1: 
	usage();sys.exit('input fasta file is missing')
if '-r' in opts.keys():
	if int(opts['1']) < 0:
		print('length of sequence should be positive'); sys.exit(0)
	seqlen=opts['-l']

filename = sys.argv[1]

try: 
	f=open(filename)
except IOError:
	print("File does not exist")

seqs={} #initialize dictionary
for line in f:
	#lets discard  the newline at the end (if any)
	line = line.rstrip()
	#distinguish header from sequence
	if line[0]=='>': #headers always start with >. OTHEROPTION line.startswith('>')
		words=line.split() #Splits hearder based on white spaces
		name=words[0][1:] #gets rid of the> (line reads >id1 - so at position 0, characters 1 to the end)
		seqs[name]= ''
	else : #sequence is not a header
		seqs[name] = seqs[name] +line
f.close()

#Number of records in the file
NumRecord = len(seqs.keys())
print("The number of records in the file is %s" % NumRecord)

#Length of sequences in the file
seqs_len = {}
for key in seqs.keys():
	seqs_len [key]= len(seqs[key])

#Sort dictionary of lengths
import operator
sorted_seqs_len = sorted(seqs_len.items(), key=operator.itemgetter(1))
print("The tupple containing sequences and IDs sorted by sequence length: %s" %sorted_seqs_len)

#Create reverse complement of original library
def RevComp(seqs):
	seqs_RevComp = {}
	value_RevComp = []
	def reverse(value):
		return value[::-1]
	def complement(value):
		basecomplement = {'A':'T', 'a':'t', 'C':'G', 'c':'g', 'T':'A', 't':'a', 'G':'C', 'g':'c'}
		letters = list(value)
		letters = [basecomplement[base]for base in letters]
		return ''.join(letters)
	for key, value in seqs.items():
		value_RevComp = complement(reverse(value))
		key_rev = key + 'R' 
		seqs_RevComp[key_rev] = value_RevComp
	return seqs_RevComp
seqs_RevComp = RevComp(seqs)

#combine forward and reverse library
seqs_All = {}
seqs_All = {**seqs, **seqs_RevComp}

#finding open reading frames
def ReadingFrame(frame, seqs):
	"This function says if a DNA sequence contains an in-frame stop codon"
	start_codon = ['ATG']
	seqs_ORF = {}
	seqs_ORF_len = {}
	for key, value in seqs.items():
		for frame in range(0, 3):
			for i in range (frame, len(value), 3) : #frame allows you to select reading frame
				codon = value[i:i+3].upper()
				if codon in start_codon:
					start = value.find('ATG')
					stop1 = value.find('TGA', start)
					stop2 = value.find('TAG', start)
					stop3 = value.find('TAA', start)
					stop = [stop1, stop2, stop3]
					fstop = min(float(i) for i in stop)
					seqs_ORF[key]= value[start:fstop]
					seqs_ORF_len[key] = len(value)
				else:
					print('No ORF found')
	return seqs_ORF_len

seqs_ORF_len = ReadingFrame(frame, seqs)
sorted_seqs_ORF_len = sorted(seqs_ORF_len.items(), key=operator.itemgetter(1))
print("The tupple containing open reading frames: %s" %sorted_seqs_ORF_len)

#find repeats - find all repeats of length n, how many times it appears and the most frquence repeat of a given length
def FindRepeats(seqs, n):
	seq_repeat = {}
	for key, value in seqs.items():
		for i in range(0, len(value) - n):
			seq_chunk = value[i:i + n]
			if seq_chunk in seq_repeat:
				seq_repeat[seq_chunk] += 1
			else:
				seq_repeat[seq_chunk] = 1	
	return seq_repeat

seqs_repeat = FindRepeats(seqs, n)
sorted_seqs_repeat = sorted(seqs_repeat.value(), key=operator.itemgetter(1))
print("The tupple containing repeats and number of repeats: %s" %sorted_seqs_repeat)
