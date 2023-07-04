def pair_with_target_sum(arr, target_sum):
    # assert arr, "arr must not be empty"
    if not isinstance(target_sum, int):
        raise TypeError(f"{target_sum} must be an integer")

    if len(arr) == 0:
        raise ValueError("arr must not be empty")

    # [1, 2, 3, 4, 6], 6), [1, 3]
    start, end = 0, len(arr) - 1

    while start < end:
        current_sum = arr[start] + arr[end]

        if current_sum == target_sum:
            return [start, end]

        if current_sum < target_sum:
            start += 1
        else:
            end -= 1

    return [-1, -1]
