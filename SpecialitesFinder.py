def palindromechecker(string):
    if string.lower()[::-1] == string.lower():
        return True
    else:
        return False


def armstrongchecker(number):
    temp = 0
    for i in str(number):
        temp += int(i) ** 3
    if temp == number:
        return True
    else:
        return False


def primechecker(number):
    tester = True
    for i in range(2, number):
        if number % i == 0:
            tester = False
            break
    return tester


def evenorodd(number):
    if number % 2 == 0:
        return True
    else:
        return False
