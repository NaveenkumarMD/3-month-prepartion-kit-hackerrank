from math import inf
def closestNumbers(arr):
    arr.sort()
    diff=float(inf)
    ans=[]
    for i in range(1,len(arr)):
        temp=abs(arr[i-1]-arr[i])
        if temp<diff:
            diff=temp
            ans.clear()
            ans.extend((arr[i-1],arr[i]))

        elif temp==diff:
            ans.extend((arr[i-1],arr[i]))

    return (ans)
closestNumbers([5 ,4, 3 ,2])