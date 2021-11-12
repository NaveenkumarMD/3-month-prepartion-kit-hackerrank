#s=12:01:PM
# Return '12:01:00'.

#s=12:01:00 AM
# Return '00:01:00'.
def timeConversion(s):
    hh=s[0:2]
    if 'PM' in s:
        hh=int(hh)+12 if hh!='12' else hh
    else:
        if hh=='12':
            hh='00'
    return (str(hh)+s[2:8])

timeConversion('12:01:00AM')