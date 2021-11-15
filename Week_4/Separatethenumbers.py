def separateNumbers(s):
    if s[0]==s:
        return print( "NO")
    for i in range(1,len(s)):
        stack=[]
        stack.append(s[:i])
        while len(''.join(stack))<len(s):
            stack.append(str(int(stack[-1])+1))
        if i==len(s)-1:
            print( "NO")
            break
        if s==''.join(stack):
            print("YES",stack[0])
            break

x=separateNumbers("13")
print(x)