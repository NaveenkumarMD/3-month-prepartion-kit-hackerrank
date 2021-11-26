
def gamingArray(arr):
    temp=0
    while arr:
        arr=arr[:arr.index(max(arr))]
        temp+=1
    print(temp)
    if temp%2==0:
        return "ANDY"
    return "BOB"

# Time limit exceeded



#[2,3,5,4,1]

def gamingArray(arr):
    temp=0
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            temp+=1
            max=arr[i]
    return "ANDY" if temp%2!=0 else "BOB"


x=gamingarray([7, 4 ,6, 5, 9])
print(x)