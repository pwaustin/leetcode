def num_trees(n):
    """
    Problem:
    Given n, how many structurally unique BSTs can store values 1 ... n?

    :type n: int
    :rtype: int

    Solution:
    Dynamic programming with memoization. Recursively consider using each value in the range of n as the root of a BST,
    then repeat for the subtrees, building the memo as you go to minimize repetition.

    Note that there is also a much more optimal solution that simply calculates the underlying series.
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
