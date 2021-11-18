import math

def maxMin(k, arr):
    l=sorted(arr)
    return (min([abs(l[i+k-1]-l[i]) for i in range(n-k+1)]))
x=maxMin(4, [1,2,3,4,10,20,30,40,100,200])
