def int_to_roman(num):
    """
    Problem:
    Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

    :type num: int
    :rtype: str

    Solution:
    In descending order of valid numerals, try removing each numeral's value from the input and adding the numeral to
    the end of the string. Repeat until the input reaches 0.
    """

    roman_tuples = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
                    (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    result = ""

    for pair in roman_tuples:
        while num >= pair[0]:
            result += pair[1]
            num -= pair[0]

    return result
