import bisect

class Index(object):
    def __init__(self, t, k): #text and k-mer length
        self.k = k #class variables
        self.index = [] #list indexs 
        for i in range (len(t) - k + 1):
            self.index.append((t[i:i+k], i)) # tupple two assoviated values
        self.index.sort()

    def query(self, p): #p = pattern
        kmer = p[:self.k]
        i = bisect.bisect_left(self.index, (kmer, -1))
        hits = []
        while i < len (self.index):
            if self.index[i] [0] != kmer:
                break
            hits.append(self.index[i][1])
            i +=1
        return hits #list of all locations in the list where the first k bases match


def query_index(p, t, index): # index created from text t
    k = index.k
    offsets = []
    for i in index.query(p): #gives back the location where the first k bases match, still have to double check the rest of p to see if it matches t
        if p[k:] == t[i + k : i + len(p)]:
            offsets.append(i)
    return offsets

#Calling
t = 'GAGACCGT'
p =s'AGA'

index = Index (t, 2) # text and k-mer length
print(query_index(p, t, index))