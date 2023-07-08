"""
https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63d923d6647c5c53032694bc

A pangram is a sentence where every letter of the English alphabet appears 
at least once.

Given a string sentence containing English letters (lower or upper-case), 
return true if sentence is a pangram, or false otherwise.

Note: The given sentence might contain other characters like digits or spaces, 
your solution should handle these too.
"""

'''
Input: sentence = "This is not a pangram"
Output: false
Explanation: The sentence doesn't contain at least one occurrence of every 
letter of the English alphabet.
'''


def checkIfPangram(sentence):
    # remove all spaces & convert to lower letters
    txt = sentence.replace(" ", "").lower()
    cache = set()
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in txt:
        if char.isalpha():
            cache.add(char)
    return len(cache) == 26
