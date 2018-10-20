def num_trees(n):
    """
    :type n: int
    :rtype: int
    """

    def unique_trees(memo, m):
        if m in memo:
            return memo[m]

        count = 0
        for i in range(0, m):
            count += unique_trees(memo, i) * unique_trees(memo, m - 1 - i)

        memo[m] = count
        return count

    return unique_trees({0: 1, 1: 1}, n)
