from heapq import heappop, heappush


def find_kth_smallest_number(nums, k):
    n = len(nums)

    if n == 0:
        return None

    # Check if k is valid
    if k < 1 or k > n:
        return None

    max_heap = []

    # for i in range(k):
    #     heappush(max_heap, -nums[i])

    # for i in range(k, n):
    #     if -nums[i] > max_heap[0]:
    #         heappop(max_heap)
    #         heappush(max_heap, -nums[i])

# Use absolute value when pushing and popping
    for i in range(k):
        heappush(max_heap, -abs(nums[i]))

    for i in range(k, n):
        if -abs(nums[i]) > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -abs(nums[i]))

    return -max_heap[0]


arr = [1, 5, 12, 2, 11, 5]
target = 3

actual = find_kth_smallest_number(arr, target)
expected = 5
print(actual == expected)
