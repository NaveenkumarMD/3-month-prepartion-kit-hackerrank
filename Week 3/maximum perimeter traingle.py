def maximumPerimeterTriangle(sticks):
    sticks=sorted(sticks,reverse=True)
    for i in range(len(sticks)-2):
        if sticks[i]<sticks[i+1]+sticks[i+2] :
            return ([sticks[i+2],sticks[i+1],sticks[i]])
    return [-1]