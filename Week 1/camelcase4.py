def res(string):    
    word=string[4:]
    key1=string[0:1]
    key2=string[2:3]
    if key2=='M':
        if '()' in word:
            word=word[0:-2]
    if key1=='S':
        arr=[]
        index=0
        for i in range(len(word)):
            if word[i].isupper():
                arr.append(word[index:i])
                index=i
        arr.append(word[index:])
        arr=[i.lower() for i in arr]
        print((' '.join(arr)).strip().rstrip())
    if key1=='C':
        arr=word.split(" ")
        arr=[i.lower() for i in arr]
        if key2=='V':
            for i in range(1,len(arr)):
                arr[i]=arr[i].capitalize()
            print((''.join(arr)).strip().rstrip())
        if key2=='C':
            arr=[i.capitalize() for i in arr]
            print(''.join(arr).rstrip().strip())
        if key2=='M':
            for i in range(1,len(arr)):
                arr[i]=arr[i].capitalize()
            s=''.join(arr)
            s+='()'
            print(s.strip().rstrip())

while(True):
    try:
        x=input()
        res(x)
    except EOFError:
        break