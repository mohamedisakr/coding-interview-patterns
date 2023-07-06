def squaring_sorted_array(arr):
    n = len(arr)
    squares = [0 for item in range(n)]
    hi_index = n - 1
    left = 0
    right = n - 1

    while left <= right:
        left_sqr = arr[left] * arr[left]
        right_sqr = arr[right] * arr[right]

        if left_sqr > right_sqr:
            squares[hi_index] = left_sqr
            left += 1
        else:
            squares[hi_index] = right_sqr
            right -= 1
        hi_index -= 1

    return squares
