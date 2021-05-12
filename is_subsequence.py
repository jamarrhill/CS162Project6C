# Name: Jamar Hill

# Date: 5/10/2021

# Description: Project 6c

#strA = abcd
#1. the length of strB has to bat least the length of strA
#strB = abnoabcdet
def is_subsequence(strA, strB):
    #Base Case
    if strA == "": #if string A is empty
        return True

    if strB == "": #if string B is empty

        return False
    #Computation Recursive Logic
    elif strA[0] == strB[0]: #If String A is equal to String B in the first position

        return is_subsequence(strA[1:], strB[1:]) #iderate to next position in sting on both strins

    elif strA[0] != strB[0]: #If both strings are ot equal at the first position

        return is_subsequence(strA, strB[1:]) #Move to the next position of String B

    else:

        return False #No remaining values

    #return is_subsequence(strA, strb[1:])

strA = "abcd"
strB = "assssbnoidddiht"

print(is_subsequence(strA, strB))