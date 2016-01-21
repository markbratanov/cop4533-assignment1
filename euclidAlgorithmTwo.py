
def getGCD(a, b):

    if b > a:
        return print(getGCD(b, a))

    if a % b == 0:
        return print(b)