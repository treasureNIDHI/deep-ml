import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    # m,n=len(a),len(a[0])
    # for i in range(m):
    #     for j in range(n):
    #         a[i][j]=a[j][i]
    # return a
    return [list(row) for row in zip(*a)]
    # for i in range(len(a)-1):
    #     for j in range(len(i)):
    #         if i==j:
    #             continue
    #         else:
    #             a[i][j]=a[j][i]
    # return a

    # for row in a:
    #     for j in range(len(row)):
    #         a[row][j]=a[j][row]
    # return a