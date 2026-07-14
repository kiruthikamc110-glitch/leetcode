// Last updated: 14/07/2026, 14:56:41
class Solution {
    public int passThePillow(int n, int time) {
     int cycle = 2 * (n - 1);
        int t = time % cycle;
     if (t < n) {
            return 1 + t;
        } else {
            return n - (t - (n - 1));
        }
    }
}