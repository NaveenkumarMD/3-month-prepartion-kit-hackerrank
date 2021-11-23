def sansaXor(arr):
    temp=len(arr)
    if temp%2==0:return 0
    res=0
    for i in range(0,temp,2):        
        res^=arr[i]
    return res