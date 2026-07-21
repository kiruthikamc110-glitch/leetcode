// Last updated: 21/07/2026, 09:32:00
1class Solution {
2    public boolean canConstruct(String ransomNote, String magazine) {
3        if (ransomNote.length() > magazine.length()) {
4            return false;
5        }
6
7        int[] charCounts = new int[26];
8        for (char c : magazine.toCharArray()) {
9            charCounts[c - 'a']++;
10        }
11        for (char c : ransomNote.toCharArray()) {
12            if (charCounts[c - 'a'] == 0) {
13                return false; 
14            }
15            charCounts[c - 'a']--;
16        }
17
18        return true;
19    }
20}