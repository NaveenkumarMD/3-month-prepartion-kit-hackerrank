def countingSort(arr):
    count=Counter(arr)
    print(count)
    return [count[i] if i in count else 0 for i in range(100)]