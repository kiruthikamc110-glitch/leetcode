// Last updated: 21/07/2026, 09:28:01
1class Solution {
2    public int strStr(String haystack, String needle) {
3        int hLen = haystack.length();
4        int nLen = needle.length();
5        
6        if (nLen > hLen) return -1;
7        for (int i = 0; i <= hLen - nLen; i++) {
8            if (haystack.substring(i, i + nLen).equals(needle)) {
9                return i;
10            }
11        }
12        
13        return -1;
14    }
15}