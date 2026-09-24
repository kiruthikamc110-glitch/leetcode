# Last updated: 24/09/2026, 20:31:13
1class Solution:
2    def countAndSay(self, n):
3        result = "1"
4
5        for _ in range(n - 1):
6            new_result = ""
7            i = 0
8
9            while i < len(result):
10                count = 1
11
12                while i + 1 < len(result) and result[i] == result[i + 1]:
13                    count += 1
14                    i += 1
15
16                new_result += str(count) + result[i]
17                i += 1
18
19            result = new_result
20
21        return result