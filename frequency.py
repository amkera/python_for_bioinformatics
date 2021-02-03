dna = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
kmer = 3


#returns a whole dictionary
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


#returns the most frequent kmer
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    #3
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words

words = FrequentWords(dna, kmer)
map = FrequencyMap(dna, kmer)

print("This is the whole map: " + str(map))
print("This is the most frequent kmer: " + str(words))
