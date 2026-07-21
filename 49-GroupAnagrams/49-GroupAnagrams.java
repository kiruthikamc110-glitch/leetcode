// Last updated: 21/07/2026, 09:30:10
1import java.util.HashMap;
2import java.util.Map;
3
4class Solution {
5    public boolean wordPattern(String pattern, String s) {
6        String[] words = s.split(" ");
7        if (pattern.length() != words.length) {
8            return false;
9        }
10        
11        Map<Character, String> charToWord = new HashMap<>();
12        Map<String, Character> wordToChar = new HashMap<>();
13        
14        for (int i = 0; i < pattern.length(); i++) {
15            char c = pattern.charAt(i);
16            String word = words[i];
17            if (charToWord.containsKey(c)) {
18                if (!charToWord.get(c).equals(word)) {
19                    return false;
20                }
21            } else {
22                charToWord.put(c, word);
23            }
24            if (wordToChar.containsKey(word)) {
25                if (wordToChar.get(word) != c) {
26                    return false;
27                }
28            } else {
29                wordToChar.put(word, c);
30            }
31        }
32        
33        return true;
34    }
35}