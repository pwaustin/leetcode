def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """

    roman_tuples = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
                    (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    result = ""

    for pair in roman_tuples:
        while num >= pair[0]:
            result += pair[1]
            num -= pair[0]

    return result
