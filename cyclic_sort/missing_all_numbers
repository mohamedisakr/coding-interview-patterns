def find_all_missing_numbers(nums: list[int]) -> list[int]:
    i = 0
    n = len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing = []
    for i in range(n):
        if nums[i] != i+1:
            missing.append(i+1)
    return missing
