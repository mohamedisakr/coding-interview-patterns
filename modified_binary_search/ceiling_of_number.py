
def search_ceiling_of_number(arr, key):
    n = len(arr)
    lo = 0
    hi = n - 1

    if n == 0:
        return -1

    if key > arr[hi]:
        return -1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if key < arr[mid]:
            hi = mid - 1
        elif key > arr[mid]:
            lo = mid+1
        else:
            return mid

    # # Check if lo is within the bounds of the array
    # if lo >= 0 and lo < n:
    #     return lo - 1   # Return the index of the ceiling element
    # else:
    #     return -1  # No ceiling element found
    return lo


'''

# ----------- function by chat gpt ----------------

import bisect


def search_ceiling_of_number(arr, key):
    n = len(arr)

    if n == 0:
        return -1

    if key > arr[n-1]:
        return -1

    # Use bisect.bisect_left to find the index of the first element that is greater than or equal to the key
    index = bisect.bisect_left(arr, key)

    # Check if the index is within the bounds of the array
    if index >= 0 and index < n:
        return index  # Return the index of the ceiling element
    else:
        return -1  # No ceiling element found
'''
