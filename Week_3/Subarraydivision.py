def birthday(s, d, m):
    count=0
    for i in range(len(s)-m+1):
        sum=0
        for j in range(i,i+m):
            sum+=s[j]
            if sum>d:
                break
        print("\n")
        if sum==d:
            count+=1
    print(count)

birthday([1,2,1,3,2], 3, 2)