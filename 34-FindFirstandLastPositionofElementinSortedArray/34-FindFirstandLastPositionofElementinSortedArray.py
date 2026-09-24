# Last updated: 24/09/2026, 20:39:59
1class Solution:
2    def multiply(self, num1, num2):
3        if num1 == "0" or num2 == "0":
4            return "0"
5
6        result = [0] * (len(num1) + len(num2))
7
8        for i in range(len(num1) - 1, -1, -1):
9            for j in range(len(num2) - 1, -1, -1):
10
11                product = int(num1[i]) * int(num2[j])
12
13                position = i + j + 1
14
15                result[position] += product
16
17                result[position - 1] += result[position] // 10
18
19                result[position] %= 10
20
21        # Remove leading zeros
22        start = 0
23        while start < len(result) - 1 and result[start] == 0:
24            start += 1
25
26        return ''.join(map(str, result[start:]))