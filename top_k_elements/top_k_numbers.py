from heapq import heappop, heappush


def find_k_largest_elements(nums, k):
    min_heap = []

    # insert first 'k' elements
    for i in range(k):
        heappush(min_heap, nums[i])

    # go through the remaining numbers of the array, if the number from
    # the array is bigger than the top(smallest) number of the min-heap,
    # remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])

    return list(min_heap)
