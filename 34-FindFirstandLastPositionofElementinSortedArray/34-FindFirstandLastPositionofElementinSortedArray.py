# Last updated: 24/09/2026, 20:49:16
1class Solution:
2    def rotate(self, matrix):
3        n = len(matrix)
4
5        # Transpose the matrix
6        for i in range(n):
7            for j in range(i + 1, n):
8                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
9
10        # Reverse each row
11        for row in matrix:
12            row.reverse()