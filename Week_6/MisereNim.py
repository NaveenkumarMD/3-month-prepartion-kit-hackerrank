def misereNim(s):
    if (set(s)=={1}) and n%2==1:
        return 'Second'
    elif (set(s)=={1}) and n%2==0:
        return 'First'
    elif reduce((lambda x,y:x^y),s):
        return 'First'
    else:
        return 'Second'
