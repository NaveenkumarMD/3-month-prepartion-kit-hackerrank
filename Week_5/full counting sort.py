def countSort(arr):
    ans=[[] for _ in range(len(arr))]
    for i,j in enumerate(arr):
        key,val=j
        if i<len(arr)//2:
            val='-'
        ans[int(key)].append(val)
    print(( ' '.join([' '.join(i) for i in ans])).strip())
