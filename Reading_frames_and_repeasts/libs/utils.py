import operator
import pprint

def open_file(filename):
    try: 
        f = open(filename)
    except IOError:
        print("File does not exist")
    return f

def create_seqs(f):
    seqs = {} #initialize dictionary
    for line in f:
        #lets discard  the newline at the end (if any)
        line = line.rstrip()
        #distinguish header from sequence
        if line[0] == '>': #headers always start with >. OTHEROPTION line.startswith('>')
            words = line.split() #Splits hearder based on white spaces
            name = words[0][1:] #gets rid of the> (line reads >id1 - so at position 0, characters 1 to the end)
            seqs[name] = ''
        else: #sequence is not a header
            seqs[name] = seqs[name] + line
    return seqs

def find_repeats(seqs, n):
    seqs_repeat = {}
    for _, value in seqs.items():
        seq_len = len(value)
        for i in range(0, seq_len - n):
            seq_chunk = value[i:i + n]
            if seq_chunk in seqs_repeat:
                seqs_repeat[seq_chunk] += 1
            else:
                seqs_repeat[seq_chunk] = 1	
    return seqs_repeat

def sort_seqs(seqs_len):
    return sorted(seqs_len.items(), key=operator.itemgetter(1))

def pretty_print(value):
    pp = pprint.PrettyPrinter(indent=2)
    return pp.pprint(value)


