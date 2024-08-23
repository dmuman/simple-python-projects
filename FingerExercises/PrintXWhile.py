def printXWhile(num: int) -> str:
    toPrint = ''
    i = 0
    while i < num:
        toPrint += 'x'
        i += 1

    return toPrint


numX = int(input('How many times should I print the letter X? '))
print(printXWhile(numX))


def printXMul(num: int) -> str:
    return 'x'*num


numX2 = int(input('How many times should I print the letter X? '))
print(printXMul(numX2))