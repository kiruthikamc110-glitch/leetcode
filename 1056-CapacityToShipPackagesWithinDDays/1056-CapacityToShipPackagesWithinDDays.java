// Last updated: 14/07/2026, 14:57:08
class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int low = 0, high = 0;
        for (int w : weights) {
            if (w > low) low = w;
            high += w;            
        }
        while (low < high) {
            int mid = (low + high) / 2;

            if (canShip(weights, days, mid)) {
                high = mid;      // try smaller capacity
            } else {
                low = mid + 1;   // need bigger capacity
            }
        }

        return low;
    }

    // check if capacity is enough
    private boolean canShip(int[] weights, int days, int cap) {
        int day = 1, load = 0;

        for (int w : weights) {
            if (load + w > cap) {
                day++;
                load = 0;
            }
            load += w;
        }

        return day <= days;
    }
}