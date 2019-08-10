#!/c/Users/Andrea/Anaconda3/python

"""
add annotation here 
Build a dictionary containing all sequences from a fasta file

"""
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

	
	