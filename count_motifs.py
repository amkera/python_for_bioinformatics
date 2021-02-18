#inputs are the motifs, a list of kmers (strings)
#output the count matrix of motifs as a dictionary of lists

def Count(Motifs):
    count = {} #final dictionary
    rows = Motifs
    row = len(rows[0]) #6
    for symbol in "ACGT":
        count[symbol] = [] #4 empty lists now exist
        for nucleotide in range(row):
            count[symbol].append(0)
            #count looks like this: {'A': [0, 0, 0, 0, 0, 0], 'C': [0, 0, 0, 0, 0, 0], 'G': [0, 0, 0, 0, 0, 0], 'T': [0, 0, 0, 0, 0, 0]}
            #added a 0 to each empty list for how many nucleotides there are in a row, 6.

    t = len(Motifs)
    for i in range(t): # for each kmer in Motifs
        for j in range(row): # for each element of the kmer
            symbol = Motifs[i][j] # assigns symbol to A, C, G, or T
            count[symbol][j] += 1 # adds 1 to the position in the list assigned to the key. when we iterate over an A, add 1 to A's count.
            # print(symbol, count[symbol][j])
    return count

print(Count([
    "AACGTG",
    "GTGCAC",
    "GTGCGT",
    "CACGTG",
    "CCCGGT"
]))


#Write a function such that
# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
