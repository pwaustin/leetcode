def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
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
