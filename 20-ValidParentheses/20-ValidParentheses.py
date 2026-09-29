# Last updated: 29/09/2026, 21:39:37
1class Solution:
2    def isValid(self, s):
3        stack = []
4
5        pairs = {
6            ')': '(',
7            ']': '[',
8            '}': '{'
9        }
10
11        for char in s:
12            if char in pairs:
13                if not stack or stack[-1] != pairs[char]:
14                    return False
15                stack.pop()
16            else:
17                stack.append(char)
18
19        return len(stack) == 0