# Last updated: 29/09/2026, 21:38:17
1class Solution:
2    def fourSum(self, nums, target):
3        nums.sort()
4        result = []
5        n = len(nums)
6
7        for i in range(n - 3):
8            if i > 0 and nums[i] == nums[i - 1]:
9                continue
10
11            for j in range(i + 1, n - 2):
12                if j > i + 1 and nums[j] == nums[j - 1]:
13                    continue
14
15                left = j + 1
16                right = n - 1
17
18                while left < right:
19                    total = nums[i] + nums[j] + nums[left] + nums[right]
20
21                    if total == target:
22                        result.append([
23                            nums[i],
24                            nums[j],
25                            nums[left],
26                            nums[right]
27                        ])
28
29                        left += 1
30                        right -= 1
31
32                        while left < right and nums[left] == nums[left - 1]:
33                            left += 1
34
35                        while left < right and nums[right] == nums[right + 1]:
36                            right -= 1
37
38                    elif total < target:
39                        left += 1
40                    else:
41                        right -= 1
42
43        return result