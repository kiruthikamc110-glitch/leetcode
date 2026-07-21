// Last updated: 21/07/2026, 09:09:17
1import java.util.*;
2
3class Solution {
4    public List<List<String>> groupAnagrams(String[] strs) {
5        if (strs == null || strs.length == 0) {
6            return new ArrayList<>();
7        }
8        
9        Map<String, List<String>> map = new HashMap<>();
10        
11        for (String str : strs) {
12            char[] charArray = str.toCharArray();
13            Arrays.sort(charArray);
14            String sortedStr = new String(charArray);
15            map.putIfAbsent(sortedStr, new ArrayList<>());
16            map.get(sortedStr).add(str);
17        }
18        
19        return new ArrayList<>(map.values());
20    }
21}