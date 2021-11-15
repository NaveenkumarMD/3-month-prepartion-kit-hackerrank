from collections import Counter
def pickingNumbers(arr):
    dit=Counter(arr)
    count=max(dit.values())
    for i in dit:
        if i+1 in dit:
            count=max(count,dit[i]+dit[i+1])
        if i-1 in dit:
            count=max(count,dit[i-1]+dit[i])
    return count


pickingNumbers([1,1,2,2,3,4,4,5,5])