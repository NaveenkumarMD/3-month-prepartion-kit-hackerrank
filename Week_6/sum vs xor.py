def sumXor(n):
    return 2**(n.bit_length()-bin(n).count('1'))
sumXor(10)

def sumXor(n):
    x=0
    for i in range(n):
        if n+i==n^i:
            x+=1
    return x