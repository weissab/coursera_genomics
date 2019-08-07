#!/c/Users/Andrea/Anaconda3/python

import sys
import getopt
from libs.utils import find_repeats


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
n = int(sys.argv[2])

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

#find repeats - find all repeats of length n, how many times it appears and the most frquence repeat of a given length

seqs_repeat = find_repeats(seqs, n)
import operator
sorted_seqs_repeat = sorted(seqs_repeat.items(), key=operator.itemgetter(1))
print("The tupple containing repeats and number of repeats: %s" % sorted_seqs_repeat)