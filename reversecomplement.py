#!/c/Users/Andrea/Anaconda3/python

"""
add annotation here 

have to write into command window: 'chmod a+x FILENAME'
adding this line makes the program executable

to run from command window: python FILENAME
"""

# add annotation here:
def reversecomplement(seq) :
	"Return the reverse complement of the dna string"
	def reverse_string(seq) :
		"returns reverse of dna string"
		return seq[::-1]
	def complement(dna)
		"Return the complement sequence string."
	basecomplement = {'A':'T', 'a':'t', 'C':'G', 'c':'g', 'T':'A', 't':'a', 'G':'C', 'g':'c'}

	seq = reverse_string(seq)
	seq = complement(seq)
	return seq