def remove_duplicates(arr):
    if len(arr) == 0:
        raise ValueError("arr must not be empty")

    non_duplicate = 1
    i = 1

    while i < len(arr):
        if arr[non_duplicate - 1] != arr[i]:
            arr[non_duplicate] = arr[i]
            non_duplicate += 1
        i += 1
    return non_duplicate
