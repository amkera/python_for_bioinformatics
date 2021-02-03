def PatternMatching(Pattern, Genome):
    positions = []

    n = len(Genome)
    k = len(Pattern)
    for i in range(n-k+1):
        if Genome[i:i+k] == Pattern:
            positions.append(i)

    return (positions)




def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count


print(PatternMatching("ATAT", "GATATATGCATATACTT"))
#returns positions at which the pattern is found in the genome

print(PatternCount("ACTGTACGATGATGTGTGTCAAAG", "TGT"))
#returnns how many times the given text appears in the Genome 
