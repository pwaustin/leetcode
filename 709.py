def to_lower_case(str):
    """
    Problem:
    Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.


    :type str: str
    :rtype: str

    Solution:
    Create an upper to lower case map via dictionary; iterate through the string applying it.
    """
    str_list = list(str)
    d = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i',
         'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's',
         'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
    for i in range(0, len(str_list)):
        if str_list[i] in d:
            str_list[i] = d[str_list[i]]
    return ''.join(str_list)

