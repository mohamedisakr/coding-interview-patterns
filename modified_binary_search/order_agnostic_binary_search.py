def binary_search(arr, key):
    if len(arr) == 0:
        return -1

    lo = 0
    hi = len(arr) - 1
    is_ascending = arr[lo] < arr[hi]

    while lo <= hi:
        mid = lo + (hi-lo) // 2

        if key == arr[mid]:
            return mid

        if is_ascending:
            if key < arr[mid]:
                hi = mid-1
            else:
                lo = mid+1
        else:
            if key > arr[mid]:
                hi = mid-1
            else:
                lo = mid+1
    return -1
