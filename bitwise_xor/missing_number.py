# https://leetcode.com/problems/missing-number/solutions/2081388/4-approaches-sorting-hash-xor-math/
def find_missing_number_sort(nums: list[int]):
    n = len(nums)
    nums.sort()

    for i in range(n):
        if nums[i] != i:
            return i

    return n


def find_missing_number_hashset(nums: list[int]):
    n = len(nums)
    hashset = set()

    for i in range(n):
        hashset.add(nums[i])

    for i in range(n+1):
        if i not in hashset:  # if hashset.add(i):
            return i

    return n


'''
arr = [1, 5, 2, 6, 4]
actual = find_missing_number_sort(arr)
expected = 3

print(f'missing number : {actual}')
print(f'actual : {actual} = expected : {expected}')
# '''

'''
arr1 = [1, 5, 2, 6, 4]
actual1 = find_missing_number_hashset(arr1)
expected1 = 3

print(f'missing number : {actual1}')
print(f'actual : {actual1} = expected : {expected1}')
'''
