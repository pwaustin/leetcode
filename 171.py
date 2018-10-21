def title_to_number(s):
    """
    Problem:
    Given a column title as appear in an Excel sheet, return its corresponding column number.

    :type s: str
    :rtype: int

    Solution: This is effectively converting from coded base 26 to base 10. Reverse s, enumerate it, convert the chars
    to corresponding ints, and build the decimal number as you would in any base conversion. Offset by -64 produces the
    appropriate conversion for capital letters A-Z.
    """

    result = 0
    s = s[::-1]

    for exponent, char in enumerate(s):
        result += (ord(char) - 64) * (26 ** exponent)

    return result
