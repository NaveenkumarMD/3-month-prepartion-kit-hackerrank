def pylons(k, arr):
    count=0
    for i in range(len(arr),k):
        if max(arr[i:i+k])==1:
            count+=1
        else:
            
x=pylons(k=2,arr = [0, 1, 1, 1, 1, 0])
print(x)