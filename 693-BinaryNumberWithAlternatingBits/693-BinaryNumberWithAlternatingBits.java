// Last updated: 14/07/2026, 15:27:10
class Solution {
    public boolean hasAlternatingBits(int n) {
     int x = n ^ (n >> 1);
        return (x & (x + 1)) == 0;    
    }
}