def miniMaxSum(arr):
    min=arr[0]
    sum=0
    max=arr[0]
    for i in arr:
        if i>max:
            max=i
        if i<min:
            min=i
        sum+=i
    print(sum-max,sum-min)