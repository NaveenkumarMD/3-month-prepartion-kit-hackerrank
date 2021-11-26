
def balancedSums(arr):
    if len(arr)==1:
        return "YES"
    s=0
    t=sum(arr)
    for i in arr:
        t-=i
        if s==t:
            return "YES"
        s+=i
    return "NO"
x=balancedSums([1,2,3])
print(x)