import collections


def longest_palindrome(s):
    """
    Problem:
    Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can
    be built with those letters. This is case sensitive, for example "Aa" is not considered a palindrome here.

    :type s: str
    :rtype: int

    Solution:
    We include the number of all the chars that occur in pairs, plus one for the first char we find that has no match,
    if any.
    """

    result = 0

    for char_count in collections.Counter(s).values():
        result += char_count // 2 * 2
        if result % 2 == 0 and char_count % 2 == 1:
            result += 1
    return result


