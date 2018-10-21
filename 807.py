def max_increase_keeping_skyline(grid):
    """
    Problem:
    In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are
    allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different
    buildings). Height 0 is considered to be a building as well.

    At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must
    be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by
    all the buildings when viewed from a distance. See the following example.

    What is the maximum total sum that the height of the buildings can be increased?

    :type grid: List[List[int]]
    :rtype: int

    Solution:
    Find the max height for all rows and columns. Each location on the grid can be increased by the min of the max
    values in its column and row, i.e. return the sum of those differences.
    """

    max_row_height = [max(row) for row in grid]
    max_col_height = [max(col) for col in zip(*grid)]

    return sum(min(max_row_height[r], max_col_height[c]) - val
               for r, row in enumerate(grid) for c, val in enumerate(row))
