import collections


def longest_palindrome(s):
    result = 0
    for char_count in collections.Counter(s).values():
        result += char_count // 2 * 2
        if result % 2 == 0 and char_count % 2 == 1:
            result += 1
    return result


