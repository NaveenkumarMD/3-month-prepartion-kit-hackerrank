def fibonacciModified(t1, t2, n):
    if n==1:
        return t1
    if n==2:
        return t2
    arr=[t1,t2]
    for i in range(2,n):
        arr.append(arr[i-2]+arr[i-1]**2)
    return arr[n-1]
x=fibonacciModified(0,1,6)
print(x)