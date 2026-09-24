# Last updated: 24/09/2026, 20:39:12
1class Solution:
2    def trap(self, height):
3        left = 0
4        right = len(height) - 1
5
6        left_max = 0
7        right_max = 0
8        water = 0
9
10        while left < right:
11
12            if height[left] <= height[right]:
13
14                if height[left] >= left_max:
15                    left_max = height[left]
16                else:
17                    water += left_max - height[left]
18
19                left += 1
20
21            else:
22
23                if height[right] >= right_max:
24                    right_max = height[right]
25                else:
26                    water += right_max - height[right]
27
28                right -= 1
29
30        return water