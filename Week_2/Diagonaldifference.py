def diagonalDifference(arr):
    main,sub=(0,0)
    for k in range(len(arr)):
        main+=arr[k][k]
    i=0
    j=len(arr)-1
    while(j>-1):
        print(arr[i][j])
        sub+=arr[i][j]
        i+=1
        j-=1
    return abs(main-sub)
x=diagonalDifference([
    [11,2,4],
    [4,5,6],
    [10,8,-12]
    ])
print(x)