def anagram(s):
    l=len(s)
    if l%2==1:
        return -1
    first=s[:l//2]
    second=s[l//2:]
    count=0
    for i in second:
        if i in first:
            first=first.replace(i,'',1)
        else:
            count+=1    
    return count 

print(anagram('xaxbbbxx'))