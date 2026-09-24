# Last updated: 24/09/2026, 20:48:14
1class Solution:
2    def permuteUnique(self, nums):
3        result = []
4        nums.sort()
5        used = [False] * len(nums)
6
7        def backtrack(current):
8            if len(current) == len(nums):
9                result.append(current[:])
10                return
11
12            for i in range(len(nums)):
13
14                if used[i]:
15                    continue
16
17                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
18                    continue
19
20                used[i] = True
21                current.append(nums[i])
22
23                backtrack(current)
24
25                current.pop()
26                used[i] = False
27
28        backtrack([])
29
30        return result