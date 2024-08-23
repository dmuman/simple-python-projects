def largestOdd() -> int | str:
    odds = []
    for i in range(10):
        number = int(input("Write an integer: "))
        if number % 2 != 0:
            odds.append(number)
    if not odds:
        return 'No odds were given'
    return max(odds)


print(largestOdd())
