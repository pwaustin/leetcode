def rotate(matrix):
    """
    Problem:

    You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
    another 2D matrix and do the rotation.

    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.

    Solution:
    For each layer of the grid that can be rotated, do a clockwise rotation on each tuple of 4 left, bottom, right, and
    top values.
    """

    n = len(matrix)

    for layer in range(0, int(n/2)):
        start = layer
        end = n - 1 - layer

        i = start
        while i < end:
            offset = i - start
            top = matrix[start][i]

            matrix[start][i] = matrix[end - offset][start]
            matrix[end - offset][start] = matrix[end][end-offset]
            matrix[end][end - offset] = matrix[i][end]
            matrix[i][end] = top

            i += 1
