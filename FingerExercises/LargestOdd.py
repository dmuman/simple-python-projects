def largestOdd(x: int, y: int, z: int) -> int:
    numbers = (x, y, z)
    odds = [num for num in numbers if num % 2 != 0]

    if len(odds) == 0:
        return min(x, y, z)

    return max(odds)
    # Time: O(1)
    # Space: O(1)


print(largestOdd(3, 5, 7))
print(largestOdd(4, 9, 5))
print(largestOdd(8, 14, 11))
print(largestOdd(2, 4, 6))
print(largestOdd(3, 3, 8))
print(largestOdd(5, 5, 5))
print(largestOdd(4, 4, 4))
print(largestOdd(7, 2, 1))
print(largestOdd(-3, -5, -2))
print(largestOdd(-4, -6, -8))


def largestOddIf(x: int, y: int, z: int) -> int:
    answer = min(x, y, z)
    if x % 2 != 0:
        answer = x
    if y % 2 != 0 and y > answer:
        answer = y
    if z % 2 != 0 and z > answer:
        answer = z

    return answer
    # Time: O(1)
    # Space: O(1)


print(largestOddIf(3, 5, 7))
print(largestOddIf(4, 9, 5))
print(largestOddIf(8, 14, 11))
print(largestOddIf(2, 4, 6))
print(largestOddIf(3, 3, 8))
print(largestOddIf(5, 5, 5))
print(largestOddIf(4, 4, 4))
print(largestOddIf(7, 2, 1))
print(largestOddIf(-3, -5, -2))
print(largestOddIf(-4, -6, -8))
