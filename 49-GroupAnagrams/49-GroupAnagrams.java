// Last updated: 21/07/2026, 09:24:23
1class Solution {
2    public boolean validPalindrome(String s) {
3        int left = 0;
4        int right = s.length() - 1;
5        
6        while (left < right) {
7            if (s.charAt(left) != s.charAt(right)) {
8                return isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1);
9            }
10            left++;
11            right--;
12        }
13        
14        return true;
15    }
16    
17    private boolean isPalindrome(String s, int left, int right) {
18        while (left < right) {
19            if (s.charAt(left) != s.charAt(right)) {
20                return false;
21            }
22            left++;
23            right--;
24        }
25        return true;
26    }
27}