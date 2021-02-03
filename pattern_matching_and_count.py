def PatternMatching(Pattern, Genome):
    positions = []

    n = len(Genome)
    k = len(Pattern)
    for i in range(n-k+1):
        if Genome[i:i+k] == Pattern:
            positions.append(i)

    return (positions)

#PatternMatching("ATAT", "GATATATGCATATACTT")



def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

print(PatternCount("ACTGTACGATGATGTGTGTCAAAG", "TGT"))
