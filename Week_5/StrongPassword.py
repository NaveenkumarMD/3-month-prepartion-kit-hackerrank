def minimumNumber(n,password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    number=1
    lower_cas=1
    upper_cas=1
    special=1
    for i in password:
        i=str(i)
        if i in numbers:
            number=0
        elif i in lower_case:
            lower_cas=0
        elif i in upper_case:
            upper_cas=0
        elif i in special_characters:
            special=0
    temp=number+lower_cas+upper_cas+special
    return temp if temp+n >6 else 6-(n+temp)+temp

x=minimumNumber(11, '#HackerRank')
print(x)