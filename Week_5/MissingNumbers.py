def func(arr,brr):
    for i in arr:
        brr.remove(i)
    return sorted(list(set(brr)))