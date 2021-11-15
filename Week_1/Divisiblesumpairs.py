
# O(n2)
import time
# def fun(arr,k):
#     length=len(arr)
#     count=0
#     for i in range(0,length-1):
#         for j in range(i+1,length):
#             if (arr[i]+arr[j])%k==0:
#                 count+=1
#     print(count)

def fun(arr,k):
    count=0
    for i in range(len(arr)):
        if k-(arr[i]%k) in arr[i+1:]:
            count+=1
    print(count)
starttime=time.time()
fun([i for i in range(900)],3)
print(time.time()-starttime)

