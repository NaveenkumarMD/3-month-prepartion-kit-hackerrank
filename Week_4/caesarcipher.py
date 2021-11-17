def caesarCipher(s, k):
    temp=""
    for i in s:
        if 65<=ord(i)<=90:
            temp+=chr(((ord(i)-65+k)%26)+65)
        elif 97<=ord(i)<=123:
            temp+=chr(((ord(i)-97+k)%26)+97)
        else:
            temp+=i
    print(temp)
caesarCipher("DNFjxo?b5h*5<LWbgs6?V5{3M].1hG)pv1VWq4(!][DZ3G)riSJ.CmUj9]7Gzl?VyeJ2dIPEW4GYW*scT8(vhu9wCr]q!7eyaoy.",45)
