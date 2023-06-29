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


def find_avg_sub_array_slide(arr, k):
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
    return result


k = 5
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(find_avg_sub_array_slide(arr, k))
