""" check if a number is happy or not
"""

'''
def is_happy_number(n):
    """ chat gpt 
    """
    # Initialize a set to store the seen numbers

    seen = set()
    # Loop until n is 1 or already seen
    while n != 1 and n not in seen:
        # Add n to the seen set
        seen.add(n)
        # Initialize a new sum
        new_sum = 0
        # Loop through each digit of n
        while n > 0:
            # Get the last digit and square it
            digit = n % 10
            new_sum += digit ** 2
            # Remove the last digit from n
            n //= 10
        # Update n with the new sum
        n = new_sum
    # Return true if n is 1, false otherwise
    return n == 1
'''


def find_square_sum(num: int) -> int:
    """ calculate the sum of the number square digits
    """
    total = 0
    while num > 0:
        digit = num % 10
        total += digit*digit
        num //= 10
    return total


def is_happy_number(n):
    """ check if a number is happy or not
    """
    if not isinstance(n, int):
        raise TypeError(f'{n} type must be int')

    if n == 1 or n == 7:
        return True

    slow = n
    fast = n

    while (True):
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))

        if slow == fast:
            break

    return (slow == 1)


'''
def main():
    print(is_happy_number(23))
    print(is_happy_number(12))


main()
'''
