def func(arr,index):
    if arr.count(0)==len(arr):
        return arr
    for i in range(index,len(arr)):
        arr[i]-=1
        func(arr,index=i)


func(arr= [2, 1, 3],index=0)