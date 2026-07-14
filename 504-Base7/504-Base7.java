// Last updated: 14/07/2026, 15:45:36
class Solution {
    public String convertToBase7(int num) {
     if (num == 0) return "0";

        boolean neg = num < 0;
        num = Math.abs(num);

        String s = "";
        while (num > 0) {
            s = (num % 7) + s;
            num /= 7;
        }

        return neg ? "-" + s : s;   
    }
}