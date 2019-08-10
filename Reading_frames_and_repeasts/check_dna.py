#!/c/Users/Andrea/Anaconda3/python

"""
add annotation here 

have to write into command window: 'chmod a+x FILENAME'
adding this line makes the program executable

to run from command window: python FILENAME
"""

# add annotation here:
dna = input('Enter DNA sequence:')

if 'n' in or 'N' in dna:
	nbases=dna.count('n') + dna.count('N')
	print ("dna sequence has %d undefined bases " % nbases)

else:
	print ("dna sequence has no undefined bases")