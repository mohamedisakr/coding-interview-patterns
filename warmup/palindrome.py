def isPalindrome(s: str) -> bool:
    txt = ''.join(ch for ch in s if ch.isalnum()).lower()
    return txt == txt[::-1]


# print(isPalindrome("A man, a plan, a canal: Panama"))
