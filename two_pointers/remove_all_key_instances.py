def remove_all_key_instances(arr, key):
    if len(arr) == 0:
        raise ValueError("arr must not be empty")

    next_item = 0

    for i, item in enumerate(arr):
        if arr[i] != key:
            arr[next_item] = arr[i]
            next_item += 1

    return next_item


'''
Key = 2
arr = [2, 11, 2, 2, 1]
res = remove_all_key_instances(arr, Key)
print(res == 2)

print()

arr = [3, 2, 3, 6, 3, 10, 9, 3]
Key = 3
res = remove_all_key_instances(arr, Key)
print(res == 4)


'''
