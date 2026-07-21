// Last updated: 21/07/2026, 09:22:20
1class Solution {
2    public int countSubstrings(String s) {
3        if (s == null || s.length() == 0) return 0;
4        
5        int totalCount = 0;
6        
7        for (int i = 0; i < s.length(); i++) {
8            totalCount += countPalindromesAroundCenter(s, i, i);
9            totalCount += countPalindromesAroundCenter(s, i, i + 1);
10        }
11        
12        return totalCount;
13    }
14    
15    private int countPalindromesAroundCenter(String s, int left, int right) {
16        int count = 0;
17        
18        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
19            count++;
20            left--;
21            right++;
22        }
23        
24        return count;
25    }
26}