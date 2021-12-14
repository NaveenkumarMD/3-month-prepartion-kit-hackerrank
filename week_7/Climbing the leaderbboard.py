def climbingLeaderboard(ranked, player):
    ranked=sorted(set(ranked),reverse=True)
    ranked=list(ranked)
    player=sorted(player,reverse=True)
    j=0
    arr=[]
    for i in range(len(player)):
        while j<len(ranked) and ranked[j]>player[i]:
            j+=1
        arr.append(j+1)
    return reversed(arr)


z=climbingLeaderboard([100,90,90,80],[70,80,105])
for i in list(reversed(z)):
    print(i)