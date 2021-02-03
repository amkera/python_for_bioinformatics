# def Reverse(Pattern):
#     rev = Pattern[::-1]
#     print (rev)

# Reverse("abcdefg")


#my code
def Reverse(Pattern):
    result = ""
    for char in Pattern:
        result = char + result
    return (result)


#my code
def Complement(Pattern):
    result = ""
    for char in Pattern:
        if char == "A":
            result+="T"
        elif char == "T":
            result+="A"
        elif char =="G":
            result+="C"
        else:
            result+="G"
    return (result)



# def Complement(Pattern):
#     dictionary = {
#         'A': 'T',
#         'T': 'A',
#         'G': 'C',
#         'C': 'G'
#     }
#
#     for char in Pattern:
#         return "".join(dictionary[i] for i in Pattern)

rev = Reverse("ATGCATGCATGC")
com = Complement(rev)


print(rev, com)
