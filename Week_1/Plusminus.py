def plusMinus(arr):
    n=len(arr)
    positive=0
    negative=0
    zero=0
    for i in arr:
        if i<0:
            negative+=1
        elif i>0:
            positive+=1
        else:
            zero+=1
    print( round(positive/n,5))
    print(round(negative/n,5))
    print(round(zero/n,5))