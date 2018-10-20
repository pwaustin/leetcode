def reverse(x):
    """
    Problem:
    Given a 32-bit signed integer, reverse digits of an integer.

    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
    [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
    overflows.

    :type x: int
    :rtype: int

    Solution:
    Pop digits from the original number and push them onto the new number; handle cases where overflow can occur.
    """

    result, max_int, min_int = 0, 2**31-1, -2**31

    while x is not 0:
        if x > 0:
            remainder = x % 10
            x = x // 10
        else:
            remainder = x % -10
            x = -(x // -10)
        if result > max_int // 10 or (result == max_int and remainder > 7):
            return 0
        if result < -(min_int // -10) or (result == min_int and remainder < -8):
            return 0

        result = result * 10 + remainder

    return result
