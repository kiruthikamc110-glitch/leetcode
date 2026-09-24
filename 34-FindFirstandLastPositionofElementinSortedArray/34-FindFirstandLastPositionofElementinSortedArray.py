# Last updated: 24/09/2026, 20:29:47
1class Solution:
2    def isValidSudoku(self, board):
3        rows = [set() for _ in range(9)]
4        cols = [set() for _ in range(9)]
5        boxes = [set() for _ in range(9)]
6
7        for i in range(9):
8            for j in range(9):
9                num = board[i][j]
10
11                if num == ".":
12                    continue
13
14                box = (i // 3) * 3 + (j // 3)
15
16                if num in rows[i]:
17                    return False
18
19                if num in cols[j]:
20                    return False
21
22                if num in boxes[box]:
23                    return False
24
25                rows[i].add(num)
26                cols[j].add(num)
27                boxes[box].add(num)
28
29        return True