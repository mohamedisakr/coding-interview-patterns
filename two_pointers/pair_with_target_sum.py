def pair_with_target_sum_2_pointers(arr, target_sum):
    # assert arr, "arr must not be empty"
    if not isinstance(target_sum, int):
        raise TypeError(f"{target_sum} must be an integer")

    if len(arr) == 0:
        raise ValueError("arr must not be empty")

    start, end = 0, len(arr) - 1

    while start < end:
        current_sum = arr[start] + arr[end]

        if current_sum == target_sum:
            return [start, end]

        if target_sum > current_sum:
            start += 1
        else:
            end -= 1

    return [-1, -1]


def pair_with_target_sum_hashtable(arr, target_sum):
    # assert arr, "arr must not be empty"
    if not isinstance(target_sum, int):
        raise TypeError(f"{target_sum} must be an integer")

    if len(arr) == 0:
        raise ValueError("arr must not be empty")

    store = {}
    for i, num in enumerate(arr):
        diff = target_sum - num
        if diff in store:
            return [store[diff], i]
        else:
            store[arr[i]] = i
    return [-1, -1]
