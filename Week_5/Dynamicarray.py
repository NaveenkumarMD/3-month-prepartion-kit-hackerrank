def dynamicArray(n, queries):
    arr=[[ ] for _ in range(n)]
    lastAnswer=0
    answer=[]
    for query in queries:
        t,x,y=query
        if t==1:
            idx=((x^lastAnswer)%n)
            arr[idx].append(y)
        if t==2:
            idx=((x^lastAnswer)%n)
            lastAnswer=arr[idx][y%len(arr[idx])]
            answer.append(lastAnswer)
    return answer