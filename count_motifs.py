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

# Explanation
# This week's lessons are about frequencies and a continuation of functions and loops. In this homework assignment, I was asked to
# make a dictionary or a map of the count matrix of a group of string kmers. This was confusing at first, and I had to search for the
# answer and reverse engineer it so I could understand the task at hand.
#
# Basically, if the input looks like this:
# ["AACGTG",
# "GTACAG",
# "GTACGG",
# "CAAGTG",
# "CCAGGG"],
#
# I need to figure out the code to output this:
#
# {'A': [1, 2, 0, 0, 1, 0], 'C': [2, 1, 3, 2, 0, 1], 'G': [2, 0, 2, 3, 2, 2], 'T': [0, 2, 0, 0, 2, 2]}
#
# where the keys are nucleotides, and the values are lists of numbers where each number corresponds to that nucleotides frequency of appearing.
# I start out by initializing a count empty dictionary, and setting row equal to the length of the first string in the input array/list.
#
# For each of the 4 nucleotides, I initialize an empty list. There are now 4 empty lists.
#
# For each nucleotide in each row, I append a 0 to the list so the count now looks like this:
#
# {'A': [0, 0, 0, 0, 0, 0], 'C': [0, 0, 0, 0, 0, 0], 'G': [0, 0, 0, 0, 0, 0], 'T': [0, 0, 0, 0, 0, 0]}
#
# About halfway there.
#
# I set t equal to the length of the input list, aka how many sequences were given. For i in range(t), or for every kmer in the list,
# and then for j in range(row), or for every nucleotide in the kmer,
# I set a symbol variable equal to whatever nucleotide we happen to be iterating on (A, C, T, G).
#
# Then, if we are iterating on a specific nucleotide, I add 1 to that nucleotide's count.
#
# I return the count to get a dictionary of the count matrix.
