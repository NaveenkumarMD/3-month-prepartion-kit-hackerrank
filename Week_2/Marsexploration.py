def marsExploration(s):
    count+=1
    for i in range(len(s)):
        if i%3 in [0,2]:
            if s[i]!='S':
                count+=1
        else:
            if s[i]!='O':
                count+=1
    return count