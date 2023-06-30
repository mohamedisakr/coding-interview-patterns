"""
Given an array, find the average of all contiguous subarrays of size 'k' in it.
"""


def find_avg_sub_array(arr, k):
    result = []
    for i in range(len(arr)-k+1):
        # print(len(arr), len(arr)-k+1)
        total = 0
        for j in range(i, i+k):
            total += arr[j]
        result.append(total/k)
    return result


def find_avg_sub_array_slide(arr: list[float], k: int):
    """Find the average of all contiguous subarrays of size k in the given array.

    This function uses a sliding window technique to iterate over the array and
    calculate the average of each subarray of size k. It returns a list of
    averages.

    Args:
        arr: The input array of numbers. Must not be empty.
        k: The size of the subarray. Must be positive and not larger than the length of the array.

    Returns:
        A list of averages of all contiguous subarrays of size k in the input array.

    Raises:
        ValueError: If k is zero or negative
        ValueError: If k is larger than the length of the array.
        TypeError: If k is not an integer.
    """
    # Check for preconditions

    # check if k is an iteger
    if not isinstance(k, int):
        raise TypeError("k must be an integer")

    # assert arr, "arr must not be empty"
    if len(arr) <= 0:
        raise ValueError("arr must not be empty")

    # assert k > 0, "k must be positive"
    if k <= 0:
        raise ValueError("k must be positive")

    # assert k <= len(arr), "k must not be larger than the length of the array"
    if k > len(arr):
        raise ValueError("k must not be larger than the length of the array")

    result = []
    total = 0.0
    start = 0
    for end, element in enumerate(arr):  # range(len(arr)):
        # print(f'index {end}, element {element}')
        total += arr[end]
        if end >= k-1:
            result.append(total/k)
            total -= arr[start]
            start += 1

    # Check for postconditions
    assert len(result) == len(arr) - k + 1, \
        "result must have the same length as the number of subarrays"

    assert all(isinstance(x, float)
               for x in result), "result must contain only floats"

    return result


k = 5
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(find_avg_sub_array_slide(arr, k))
