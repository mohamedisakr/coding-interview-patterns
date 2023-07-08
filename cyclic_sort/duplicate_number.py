""" find duplicate using cyclic sort
"""


def find_duplicate(nums: list[int]) -> int:
    """ find duplicate using cyclic sort
    """
    # if all(not isinstance(item, int) for item in nums):
    #     raise TypeError("all elements must be of type int")

    # if not isinstance(nums, list(int)):
    #     raise TypeError("all elements must be of type int")

    i = 0
    n = len(nums)

    while i < n:
        # checks if the element at index i matches i+1.
        # This is because if the list is sorted,
        # then each element should be equal to its index plus one.
        # For example, in [1, 2, 3, 4], the element at index 0 is 1,
        # the element at index 1 is 2, and so on.
        if nums[i] != i+1:
            # j store the value of nums[i]-1.
            # This is because j represents the index where nums[i]
            # should be if the list is <<sorted>>.
            # For example, if nums[i] is 4, then j should be 3.
            j = nums[i] - 1
            if nums[i] != nums[j]:
                # nums[i] is out of place and needs to be swapped with nums[j]
                # nums[i] goes to its correct position and nums[j] comes
                # to index i for further checking
                nums[i], nums[j] = nums[j], nums[i]
            else:
                # nums[i] is a duplicate and the function returns it
                # as the output.
                return nums[i]
        else:
            # If the element at index i matches i+1, then it means that
            # the element is in its correct position and the function
            # increments i by one to move to the next index.
            i += 1

    return -1


arr = [1, 4, 4, 3, 2]
res = find_duplicate(arr)
print(res == 4)
