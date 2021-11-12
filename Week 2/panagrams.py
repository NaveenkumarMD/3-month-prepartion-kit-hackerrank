def pangrams(s):
    arr=[i for i in range(97,123)]
    for i in s:
        fun=ord(i.lower())
        if fun in arr:
            arr.remove(fun)
    return 'pangram' if len(arr)==0 else 'not pangram'

pangrams('We promptly judged antique ivory buckles for the prize')