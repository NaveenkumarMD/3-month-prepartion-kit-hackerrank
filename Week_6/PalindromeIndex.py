
def ispalindrome(s):return s==s[::-1]
def palindromeindex(s):
    i,j=0,len(s)-1
    while i<j and s[i]==s[j]:
        i+=1
        j-=1
    if ispalindrome(s[i:j]):
        return j
    if ispalindrome(s[i+1:j+1]):
        return i
    return -1
palindromeindex('abcddcda')


# time limit exceeds
# def ispalindrome(s):
#     return s[::-1]==s
# def palindromeIndex(s):
#     if(ispalindrome(s)):
#         return -1
#     x=s[::-1]
#     for i in range(len(s)):
#         if (ispalindrome(s[:i]+s[i+1:])):
#             return i
#     return -1  
# c=palindromeIndex('bcbc')
# print(c)