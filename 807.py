def max_increase_keeping_skyline(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_row_height = [max(row) for row in grid]
        max_col_height = [max(col) for col in zip(*grid)]

        return sum(min(max_row_height[r], max_col_height[c]) - val
                   for r, row in enumerate(grid) for c, val in enumerate(row))
