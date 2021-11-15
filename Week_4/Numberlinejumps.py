def kangaroo(x1, v1, x2, v2):
    if v1<=v2:
        return "NO"
    if x1==x2:
        return "YES"
    if (x1-x2)%(v1-v2)==0:
        return "YES"
    else:
        return "NO"