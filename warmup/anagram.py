def is_anagram(s, t):
    # If the lengths of the strings are different, they cannot be anagrams
    if len(s) != len(t):
        return False

    # Create a dictionary to store the frequency of each character in s
    s_dict = {}
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in s_dict:
            s_dict[char] += 1
        # Otherwise, initialize its count to 1
        else:
            s_dict[char] = 1

    # Loop through each character in t
    for char in t:
        # If the character is not in the dictionary, or its count is zero,
        # they are not anagrams
        if char not in s_dict or s_dict[char] == 0:
            return False
        # Otherwise, decrement its count by 1
        else:
            s_dict[char] -= 1

    # If the loop finishes without returning False, they are anagrams
    return True


# These are anagrams
s1 = "listen"
t1 = "silent"

# These are not anagrams
s2 = "apple"
t2 = "orange"

# These are not anagrams
s3 = "rat"
t3 = "car"


# These are not anagrams
s4 = "hello"
t4 = "world"


# Print the results of calling the function with these pairs of strings
print(is_anagram(s1, t1))  # True
print(is_anagram(s2, t2))  # False
print(is_anagram(s3, t3))  # False
print(is_anagram(s3, t3))  # False
