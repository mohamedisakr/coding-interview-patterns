"""
https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63d8efe7f8694f3655d60712
Given an integer array nums, return true if any value appears at 
least twice in the array, and return false if every element is distinct.
"""


def containsDuplicate(nums):
    """
    3 approaches
    1. Approach 1: Brute Force
    2. Approach 2: Using Hash Set
    3. Approach 3: Sorting    
    """

    unique_cache = set()

    for item in nums:
        if item in unique_cache:
            return True
        unique_cache.add(item)
    return False
