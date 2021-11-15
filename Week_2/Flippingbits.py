def flippingBits(n):
    binaryform=format(n,'b').zfill(32)
    arr=['0' if i=='1' else '1' for i in binaryform]
    arr=''.join(arr)
    x=int()
    print(x)
flippingBits(23)