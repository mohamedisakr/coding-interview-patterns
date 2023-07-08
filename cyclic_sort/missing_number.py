""" find the missing number in an array containing 'n' 
    distinct numbers taken from the range 0 to 'n'
"""


def find_missing_number(nums: list[int]) -> int:
    """ find the missing number in an array containing 'n' 
    distinct numbers taken from the range 0 to 'n'
    """
    i = 0
    n = len(nums)

    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return n


print(find_missing_number([4, 0, 3, 1]))
