def migratoryBirds(arr):
    from collections import Counter
    dit=Counter(arr)
    tempid=math.inf
    temp=0
    for i,j in dit.items():
        if j>temp:
            temp=j
            tempid=i
        elif j==temp:
            tempid=min(tempid,i)
    return tempid