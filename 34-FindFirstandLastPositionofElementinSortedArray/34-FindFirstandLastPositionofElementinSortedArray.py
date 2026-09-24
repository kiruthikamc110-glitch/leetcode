# Last updated: 24/09/2026, 20:56:25
1class Solution:
2    def totalNQueens(self, n):
3        count = [0]
4
5        cols = set()
6        diag1 = set()
7        diag2 = set()
8
9        def backtrack(row):
10            if row == n:
11                count[0] += 1
12                return
13
14            for col in range(n):
15
16                if col in cols:
17                    continue
18
19                if row - col in diag1:
20                    continue
21
22                if row + col in diag2:
23                    continue
24
25                # Place queen
26                cols.add(col)
27                diag1.add(row - col)
28                diag2.add(row + col)
29
30                backtrack(row + 1)
31
32                # Remove queen
33                cols.remove(col)
34                diag1.remove(row - col)
35                diag2.remove(row + col)
36
37        backtrack(0)
38
39        return count[0]