# Last updated: 24/09/2026, 20:32:45
1class Solution:
2    def combinationSum(self, candidates, target):
3        result = []
4
5        def backtrack(start, current, total):
6            if total == target:
7                result.append(current[:])
8                return
9
10            if total > target:
11                return
12
13            for i in range(start, len(candidates)):
14                current.append(candidates[i])
15
16                backtrack(i, current, total + candidates[i])
17
18                current.pop()
19
20        backtrack(0, [], 0)
21
22        return result