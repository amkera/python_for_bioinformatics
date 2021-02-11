#Hamming Distance is the number of letters that are different between the 2 input strings
def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count+=1
    return count

print (HammingDistance("ATGCATGCATGC", "ATACATGCATGC"))
