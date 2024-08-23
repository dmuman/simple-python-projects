def isPrime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


# def odds() -> list[int]:
#     return [num for num in range(2, 1000) if num % 2 != 0]
#
#
# def primes(l: list) -> list[int]:
#     return [prime for prime in l if isPrime(prime)]


def calculateSum():
    # return sum(primes(odds()))
    sumPrimes = 0
    for i in range(3, 1000, 2):
        if isPrime(i):
            sumPrimes += i
    return sumPrimes


print(calculateSum())
