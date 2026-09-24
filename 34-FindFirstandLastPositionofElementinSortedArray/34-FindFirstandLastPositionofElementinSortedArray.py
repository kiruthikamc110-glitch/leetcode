# Last updated: 24/09/2026, 21:59:52
1class Solution:
2    def spiralOrder(self, matrix):
3        result = []
4
5        top = 0
6        bottom = len(matrix) - 1
7        left = 0
8        right = len(matrix[0]) - 1
9
10        while top <= bottom and left <= right:
11
12            # Left → Right
13            for col in range(left, right + 1):
14                result.append(matrix[top][col])
15            top += 1
16
17            # Top → Bottom
18            for row in range(top, bottom + 1):
19                result.append(matrix[row][right])
20            right -= 1
21
22            # Right → Left
23            if top <= bottom:
24                for col in range(right, left - 1, -1):
25                    result.append(matrix[bottom][col])
26                bottom -= 1
27
28            # Bottom → Top
29            if left <= right:
30                for row in range(bottom, top - 1, -1):
31                    result.append(matrix[row][left])
32                left += 1
33
34        return result