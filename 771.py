def num_jewels_in_stones(J, S):
    """
    Problem:

    You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
    Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

    The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so
    "a" is considered a different type of stone from "A".

    :type J: str
    :type S: str
    :rtype: int

    Solution:
    Enumerate J, increment the number of jewels for all of J's values found in S.
    """
    result = 0
    for index, char in enumerate(J):
        result += S.count(char)
    return result

