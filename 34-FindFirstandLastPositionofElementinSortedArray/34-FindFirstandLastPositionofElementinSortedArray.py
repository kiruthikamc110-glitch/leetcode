# Last updated: 24/09/2026, 20:28:02
1class Solution:
2    def searchRange(self, nums, target):
3        first = -1
4        last = -1
5
6        # Find first position
7        low = 0
8        high = len(nums) - 1
9
10        while low <= high:
11            mid = (low + high) // 2
12
13            if nums[mid] == target:
14                first = mid
15                high = mid - 1
16            elif nums[mid] < target:
17                low = mid + 1
18            else:
19                high = mid - 1
20
21        # Find last position
22        low = 0
23        high = len(nums) - 1
24
25        while low <= high:
26            mid = (low + high) // 2
27
28            if nums[mid] == target:
29                last = mid
30                low = mid + 1
31            elif nums[mid] < target:
32                low = mid + 1
33            else:
34                high = mid - 1
35
36        return [first, last]