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

sequences = {1: 'ATGCCCTAG', 2: 'ATGAAAAAA'}
Answer = ReadingFrame(1, sequences)