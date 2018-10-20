def reverse(x):
    """
    :type x: int
    :rtype: int
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
