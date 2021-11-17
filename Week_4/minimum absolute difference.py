import math
def minimumAbsoluteDifference(arr):
    arr=arr.sort()
    minx=arr[1]-arr[0]
    for i in range(2,len(arr)):
        if arr[i]-arr[i-1]<minx:
            minx=arr[i]-arr[i-1]
    return minx
x=minimumAbsoluteDifference([1 ,-3 ,71, 68, 17])
print(x)