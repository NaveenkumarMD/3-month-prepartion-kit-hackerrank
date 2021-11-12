def twoArrays(k, A, B):
    a=sorted(A)
    b=sorted(B,reverse=True)
    for i in range(len(a)):
        if (a[i]+b[i])<k:
            return "NO"
    return "YES"