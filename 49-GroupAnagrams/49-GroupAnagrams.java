// Last updated: 21/07/2026, 09:20:26
1class Solution {
2    public String multiply(String num1, String num2) {
3        if ("0".equals(num1) || "0".equals(num2)) {
4            return "0";
5        }
6        
7        int m = num1.length();
8        int n = num2.length();
9        int[] pos = new int[m + n];
10        for (int i = m - 1; i >= 0; i--) {
11            for (int j = n - 1; j >= 0; j--) {
12                int mul = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
13                int p1 = i + j;
14                int p2 = i + j + 1;
15                
16                int sum = mul + pos[p2];
17                
18                pos[p1] += sum / 10;
19                pos[p2] = sum % 10;
20            }
21        }
22        StringBuilder sb = new StringBuilder();
23        for (int p : pos) {
24            if (!(sb.length() == 0 && p == 0)) {
25                sb.append(p);
26            }
27        }
28        
29        return sb.length() == 0 ? "0" : sb.toString();
30    }
31}