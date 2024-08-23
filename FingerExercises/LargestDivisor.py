def largestSmallestDivisor(num: int) -> int | str:
    smallestDivisor = None
    for guess in range(2, num):
        if num % guess == 0:
            smallestDivisor = guess
            break
    if smallestDivisor:
        return num//smallestDivisor
    else:
        return f'{num} is a prime number'


print(largestSmallestDivisor(10))


def largestDivisor(num: int) -> int | str:
    largestDivisorVar = None
    for guess in range(2, num):
        if num % guess == 0:
            largestDivisorVar = num // guess
            break

    if largestDivisorVar:
        return largestDivisorVar
    else:
        return f'{num} is a prime number'


print(largestDivisor(10))
