from collections import Counter
def sockMerchant(n, ar):
    pairs=0
    dit=Counter(ar)
    for j in dit.values():
        temp=j//2
        if temp>0:
            pairs+=temp
    return pairs