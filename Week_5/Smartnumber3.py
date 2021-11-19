def is_smart_number(num):
    val = int(math.sqrt(num))
    if val**2==num:
        return True
    return False