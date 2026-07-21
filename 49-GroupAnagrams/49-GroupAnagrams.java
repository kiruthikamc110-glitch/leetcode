// Last updated: 21/07/2026, 09:26:25
1import java.util.Arrays;
2
3class Solution {
4    public boolean closeStrings(String word1, String word2) {
5        if (word1.length() != word2.length()) {
6            return false;
7        }
8
9        int[] count1 = new int[26];
10        int[] count2 = new int[26];
11
12        for (char c : word1.toCharArray()) {
13            count1[c - 'a']++;
14        }
15        for (char c : word2.toCharArray()) {
16            count2[c - 'a']++;
17        }
18        for (int i = 0; i < 26; i++) {
19            if ((count1[i] == 0 && count2[i] != 0) || (count1[i] != 0 && count2[i] == 0)) {
20                return false;
21            }
22        }
23        Arrays.sort(count1);
24        Arrays.sort(count2);
25
26        return Arrays.equals(count1, count2);
27    }
28}