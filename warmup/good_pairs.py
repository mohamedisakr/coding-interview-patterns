def num_good_pairs(nums: list[int]) -> int:
    # initialize a dictionary to store the frequency of each number
    freq = {}
    # initialize a variable to store the number of good pairs
    count = 0
    # loop through the array
    for num in nums:
        # if the number is already in the dictionary, it means we have seen it before
        # so we can add its frequency to the count, since each previous occurrence
        # can form a good pair with the current one
        if num in freq:
            count += freq[num]
        # increment the frequency of the number by one
        freq[num] = freq.get(num, 0) + 1
    # return the final count
    return count


nums1 = [1, 2, 3, 1, 1, 3]
actual = num_good_pairs(nums1)
expected = 4
print(actual == expected)
