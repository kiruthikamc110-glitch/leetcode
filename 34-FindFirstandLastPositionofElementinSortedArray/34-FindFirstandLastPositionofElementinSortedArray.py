# Last updated: 24/09/2026, 20:54:10
1class Solution:
2    def solveNQueens(self, n):
3        result = []
4        board = [["."] * n for _ in range(n)]
5
6        cols = set()
7        diag1 = set()
8        diag2 = set()
9
10        def backtrack(row):
11            if row == n:
12                result.append(["".join(r) for r in board])
13                return
14
15            for col in range(n):
16
17                if col in cols:
18                    continue
19
20                if row - col in diag1:
21                    continue
22
23                if row + col in diag2:
24                    continue
25
26                # Place queen
27                board[row][col] = "Q"
28                cols.add(col)
29                diag1.add(row - col)
30                diag2.add(row + col)
31
32                backtrack(row + 1)
33
34                # Remove queen
35                board[row][col] = "."
36                cols.remove(col)
37                diag1.remove(row - col)
38                diag2.remove(row + col)
39
40        backtrack(0)
41
42        return result