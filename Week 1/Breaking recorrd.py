def breakingRecords(scores):
    max=scores[0]
    min=scores[0]
    mincount=0
    maxcount=0
    for i in scores:
        if i>max:
            max=i
            maxcount+=1
        if i<min:
            min=i
            mincount+=1
    return [maxcount,mincount]

y=breakingRecords([3 ,4, 21, 36, 10, 28, 35, 5, 24, 42])
print(y)