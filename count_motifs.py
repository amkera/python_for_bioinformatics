#inputs are the motifs, a list of kmers (strings)
#output the count matrix of motifs as a dictionary of lists

def Count(Motifs):
    count = {} #final dictionary
    rows = Motifs
    row = len(rows[0]) #6
    for symbol in "ACGT":
        count[symbol] = []
        for nucleotide in range(row):
            count[symbol].append(0)
    #count looks like this: {'A': [0, 0, 0, 0, 0, 0], 'C': [0, 0, 0, 0, 0, 0], 'G': [0, 0, 0, 0, 0, 0], 'T': [0, 0, 0, 0, 0, 0]}
    










print(Count([
    "AACGTG",
    "GTGCAC",
    "GTGCGT",
    "CACGTG",
    "CCCGGT"
]))
