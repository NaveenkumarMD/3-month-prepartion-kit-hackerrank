def check(i):

    if i<38:
        return i
    else:
        if i%5>=3:
            return i+(5-(i%5))
        else:
            return i


def gradingStudents(grades):
    return [check(i) for i in grades]
