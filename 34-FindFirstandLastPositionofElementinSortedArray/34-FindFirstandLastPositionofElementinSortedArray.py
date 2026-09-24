# Last updated: 24/09/2026, 20:38:27
1class Solution:
2    def firstMissingPositive(self, nums):
3        n = len(nums)
4
5        for i in range(n):
6            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
7                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
8
9        for i in range(n):
10            if nums[i] != i + 1:
11                return i + 1
12
13        return n + 1