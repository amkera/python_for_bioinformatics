dna = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
kmer = 3

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if Text[i:i+k] == Pattern:
                freq[Pattern]+=1

    return (freq)


#FrequencyMap(dna, kmer)


#now return a list with most frequent kmers

# words = []
# frequencies = FrequencyMap(Text, k)

# most_frequent_kmers = max(frequencies.values())


def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    print (freq)
    m = max(freq.values())
    #3
    for key in freq:
        if freq[key] == m:
            words.append(key)
    print (words)
    return words

FrequentWords(dna, kmer)
