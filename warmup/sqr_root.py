"""
https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63d9065f4c5ef6536969a6ab
"""


def sqrt(n):
    if n < 0:
        raise ValueError("n must be positive integer")

    if not isinstance(n, (int, float)):
        raise TypeError("n must be int type")

    if n < 2:
        return n

    left = 2
    right = n//2
    num = 0

    while left <= right:
        pivot = left + (right-left)//2
        num = pivot*pivot

        if num > n:
            right = pivot-1
        elif num < n:
            left = pivot+1
        else:
            return pivot

    return right
