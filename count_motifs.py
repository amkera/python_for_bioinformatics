#inputs are the motifs, a list of kmers (strings)
#output the count matrix of motifs as a dictionary of lists

def Count(Motifs):
    count = {} #final dictionary
    k = len(Motifs[0]) #6
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)










print(Count([
    "AACGTG",
    "GTGCAC",
    "GTGCGT",
    "CACGTG",
    "CCCGGT"
]))
