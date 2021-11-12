def countingValleys(steps, path):
    x=1 if path[0]=='U' else -1
    count=0
    for i in range(1,steps):
        if path[i]=='U':
            x+=1
            if x==0:
                count+=1
        else:
            x-=1
        
    return count
x=countingValleys(8,'UDDDUDUU')
print(x)