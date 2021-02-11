def SkewArray(Genome):
    skew = [0]
    score = {"A":0, "T":0, "C":-1, "G":1}
    for i in range(1,len(Genome)+1):
            skew.append(score[Genome[i-1]] + skew[i-1])
            print("This is score[Genome[i-1]]: " + str(score[Genome[i-1]]))
            print(skew[i-1])
    return skew


print(SkewArray("CATGGGCATCGGCCATACGCC"))


# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    Positions = []
    Array = SkewArray(Genome)
    m = min(Array)
    for i in range(len(Array)):
        if Array[i] == m:
            Positions.append(i)
    return Positions
