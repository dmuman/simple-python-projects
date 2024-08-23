def rootPower(num: int) -> list[int]:
    answer = None
    for power in range(2, 6):
        root = round(num ** (1/power))
        if root ** power == num:
            answer = [root, power]

    return answer

print(rootPower(64))