// Last updated: 21/07/2026, 09:07:14
1class Solution {
2    public int lengthOfLongestSubstring(String s) {
3        int[] lastSeen = new int[128];
4        java.util.Arrays.fill(lastSeen, -1);
5        
6        int maxLength = 0;
7        int left = 0;
8        for (int right = 0; right < s.length(); right++) {
9            char currChar = s.charAt(right);
10            if (lastSeen[currChar] >= left) {
11                left = lastSeen[currChar] + 1;
12            }
13            lastSeen[currChar] = right;
14            maxLength = Math.max(maxLength, right - left + 1);
15        }
16        
17        return maxLength;
18    }
19}