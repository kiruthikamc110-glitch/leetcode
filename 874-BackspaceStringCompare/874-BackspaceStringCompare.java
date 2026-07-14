// Last updated: 14/07/2026, 14:57:41
class Solution {
    public boolean backspaceCompare(String s, String t) {
        return buildString(s).equals(buildString(t));
    }
    
    private String buildString(String str) {
        StringBuilder sb = new StringBuilder();
        for (char c : str.toCharArray()) {
            if (c != '#') {
                sb.append(c);
            } else if (sb.length() > 0) {
                // Backspace: remove the last character
                sb.deleteCharAt(sb.length() - 1);
            }
        }
        return sb.toString();
    }
}