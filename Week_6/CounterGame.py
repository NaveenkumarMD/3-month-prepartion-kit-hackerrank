def counterGame(n):
    arr=[1]
    i=1
    while arr[-1]<n:
        arr.append(2**i)
        i+=1 
    print(arr)
    def closest(x):
        i=0
        while True:
            if arr[i]>x:
                break
            a=arr[i]
            i+=1
        return a
  
    count=0
    while n!=1:
        if n in arr:
            n//=2
        else:
            c=closest(n)
            n=n-c
        count+=1
    return "Richard" if count%2==0 else "Louise"
x=counterGame(132)
print(x)