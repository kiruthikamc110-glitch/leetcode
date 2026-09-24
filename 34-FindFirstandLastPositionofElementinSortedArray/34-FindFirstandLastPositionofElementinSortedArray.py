# Last updated: 24/09/2026, 20:57:21
1class Solution:
2    def maxSubArray(self, nums):
3        current = nums[0]
4        maximum = nums[0]
5
6        for i in range(1, len(nums)):
7            current = max(nums[i], current + nums[i])
8            maximum = max(maximum, current)
9
10        return maximum