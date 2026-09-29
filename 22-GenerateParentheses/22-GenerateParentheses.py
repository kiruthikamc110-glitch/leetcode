# Last updated: 29/09/2026, 21:41:51
1class Solution:
2    def generateParenthesis(self, n):
3        result = []
4
5        def backtrack(current, open_count, close_count):
6            if len(current) == 2 * n:
7                result.append(current)
8                return
9
10            if open_count < n:
11                backtrack(current + "(", open_count + 1, close_count)
12
13            if close_count < open_count:
14                backtrack(current + ")", open_count, close_count + 1)
15
16        backtrack("", 0, 0)
17
18        return result