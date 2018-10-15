def num_jewels_in_stones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    result = 0
    for index, char in enumerate(J):
        result += S.count(char)
    return result

