// Last updated: 21/07/2026, 09:14:14
1class Solution {
2    public String longestPalindrome(String s) {
3        if (s == null || s.length() < 1) return "";
4        
5        int start = 0, end = 0;
6        
7        for (int i = 0; i < s.length(); i++) {
8            int len1 = expandAroundCenter(s, i, i);
9            int len2 = expandAroundCenter(s, i, i + 1);
10            
11            int maxLen = Math.max(len1, len2);
12            if (maxLen > end - start) {
13                start = i - (maxLen - 1) / 2;
14                end = i + maxLen / 2;
15            }
16        }
17        
18        return s.substring(start, end + 1);
19    }
20    
21    private int expandAroundCenter(String s, int left, int right) {
22        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
23            left--;
24            right++;
25        }
26        return right - left - 1;
27    }
28}