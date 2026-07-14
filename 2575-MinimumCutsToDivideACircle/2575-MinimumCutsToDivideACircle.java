// Last updated: 14/07/2026, 14:56:42
class Solution {
    public int numberOfCuts(int n) {
       if (n == 1) return 0;
        if (n % 2 == 0) return n / 2;
        return n;  
    }
}