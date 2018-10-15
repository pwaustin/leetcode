def to_lower_case(str):
    """
    :type str: str
    :rtype: str
    """
    str_list = list(str)
    d = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i',
         'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's',
         'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
    for i in range(0, len(str_list)):
        if str_list[i] in d:
            str_list[i] = d[str_list[i]]
    return ''.join(str_list)


print(to_lower_case("LOVELY"))
