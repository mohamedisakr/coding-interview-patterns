import math


def smallest_subarray_with_given_sum(arr: list[int], s: int):
    """find the length of the smallest contiguous subarray whose sum is 
    greater than or equal to 's'. Return 0, if no such subarray exists.

    This function uses a sliding window technique to iterate over the array and
    calculate the smallest contiguous subarray whose sum is greater than or 
    equal to 's'. Return 0, if no such subarray exists.

    Args:
        arr: The input array of numbers. Must not be empty.

        s: The sum of the subarray. Must be positive and 
            not larger than the sum of the array.

    Returns:
        the smallest contiguous subarray whose sum is greater than 
        or equal to 's'. Return 0, if no such subarray exists.

    Raises:
        ValueError: If s is zero or negative
        ValueError: If s is larger than the sum of the array.
        ValueError: If the array is empty.
        ValueError: If array element is negative.
        TypeError: If s is not an integer.
    """
    # Check for preconditions

    # if s > sum(arr), then return 0
    if s > sum(arr):
        return 0

    # check if s is an iteger
    if not isinstance(s, int):
        raise TypeError("s must be an integer")

    # assert arr, "arr must not be empty"
    if len(arr) <= 0:
        raise ValueError("arr must not be empty")

    # assert s > 0, "s must be positive"
    if s <= 0:
        raise ValueError("s must be positive")

    # assert k <= len(arr), "k must not be larger than the length of the array"
    if s > sum(arr):
        raise ValueError("s must not be larger than the sum of the array")

    # arr must be array of positive numbers
    if any(item < 0 for item in arr):
        raise ValueError("all elements must be positive")

    min_len = math.inf
    total = 0
    start = 0

    for end, element in enumerate(arr):  # range(len(arr)):
        total += arr[end]
        while total >= s:
            min_len = min(min_len, end-start+1)
            total -= arr[start]
            start += 1

    if min_len == math.inf:
        return 0

    return min_len


'''
print('test case 1')
arr = [2, 1, 5, 2, 3, 2]
s = 7
actual = smallest_subarray_with_given_sum(arr, s)
print(f'actual = {actual}, expected = {2}, then {actual == 2}')

print('')

print('test case 2')
arr = [2, 1, 5, 2, 8]
s = 7
actual = smallest_subarray_with_given_sum(arr, s)
print(f'actual = {actual}, expected = {1}, then {actual == 1}')

print('')

print('test case 3')
arr = [3, 4, 1, 1, 6]
s = 8
actual = smallest_subarray_with_given_sum(arr, s)
print(f'actual = {actual}, expected = {3}, then {actual == 3}')
# '''
