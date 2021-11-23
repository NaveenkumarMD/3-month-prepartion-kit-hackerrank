def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i]=sorted(grid[i])
    for i in range(len(grid[0])):
        for j in range(1,len(grid)):
            if grid[j][i]<grid[j-1][i]:
                return False
    return True

x=gridChallenge(grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])
print(x)