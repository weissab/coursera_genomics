#!/c/Users/Andrea/Anaconda3/python

"""
add annotation here 

have to write into command window: 'chmod a+x FILENAME'
adding this line makes the program executable

to run from command window: python FILENAME
"""

# add annotation here:
dna = input("Enter a DNA sequence, please:")

def has_stop_codon(dna, frame==0) : #set default value of 0 for frame
	"This function says if a DNA sequence contains an in-frame stop codon"
	stop_codon_found = Flase
	stop_codons = ['tga', 'tag', 'taa']
	for i in range (frame, len(dna), 3) : #frame allows you to select reading frame
		codon = dna[i:i+3].lower()
		if codon in stop_codons :
			stop_codon_found= True
			break
	return stop_codon_found
		