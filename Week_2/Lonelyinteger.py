def lonelyinteger(a):
    arr=[]
    for i in a:
        if i not in arr:
            arr.append(i)
        else:
            arr.remove(i)
    return arr[0]