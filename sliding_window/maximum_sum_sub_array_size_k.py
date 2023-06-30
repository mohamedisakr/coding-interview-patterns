""" 
Find the maximum sum of any contiguous sub-array of size k.
"""


def max_sum_sub_array(arr: list[int], k: int):
    """Find the maximum sum of any contiguous sub-array of size k in the given 
    array.

    This function uses a sliding window technique to iterate over the array and
    calculate the maximum sum of any contiguous subarray of size k. 
    It returns max sum.

    Args:
        arr: The input array of numbers. Must not be empty.

        k: The size of the subarray. Must be positive and 
            not larger than the length of the array.

    Returns:
        A maximum sum of any contiguous sub-array of size k.

    Raises:
        ValueError: If k is zero or negative
        ValueError: If k is larger than the length of the array.
        ValueError: If the array is empty.
        ValueError: If array element is negative.
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

    # arr must be array of positive numbers
    if any(item < 0 for item in arr):
        raise ValueError("all elements must be positive")

    max_sum = 0
    total = 0
    start = 0
    for end, element in enumerate(arr):  # range(len(arr)):
        total += arr[end]
        if end >= k-1:
            max_sum = max(total, max_sum)
            total -= arr[start]
            start += 1

    # Check for postconditions
    # assert len(result) == len(arr) - k + 1, \
    #     "result must have the same length as the number of subarrays"

    # assert all(isinstance(x, float)
    #            for x in result), "result must contain only floats"

    return max_sum


'''
print('test case 1')
arr = [2, 1, 5, 1, 3, 2]
k = 3
actual = max_sum_sub_array(arr, k)
print(f'actual = {actual}, expected = {9}, then {actual == 9}')

print('')

print('test case 2')
arr = [2, 3, 4, 1, 5]
k = 2
actual = max_sum_sub_array(arr, k)
print(f'actual = {actual}, expected = {7}, then {actual == 7}')

print('')

print('test case 3')
arr = [100, 200, 300, 400]
k = 2
actual = max_sum_sub_array(arr, k)
print(f'actual = {actual}, expected = {700}, then {actual == 700}')

print('')

print('test case 4')
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
actual = max_sum_sub_array(arr, k)
print(f'actual = {actual}, expected = {39}, then {actual == 39}')

# Input  : arr[] = {2, 3}, k = 3
# Output : Invalid
# Explanation: There is no subarray of size 3 as size of whole array is 2
'''
