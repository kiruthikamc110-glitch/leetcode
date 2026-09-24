# Last updated: 24/09/2026, 20:47:17
1class Solution:
2    def permute(self, nums):
3        result = []
4
5        def backtrack(current):
6            if len(current) == len(nums):
7                result.append(current[:])
8                return
9
10            for num in nums:
11                if num not in current:
12                    current.append(num)
13
14                    backtrack(current)
15
16                    current.pop()
17
18        backtrack([])
19
20        return result