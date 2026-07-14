// Last updated: 14/07/2026, 14:56:40
class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
    int sum = 0;

        int takeOnes = Math.min(numOnes, k);
        sum += takeOnes;
        k -= takeOnes;

        int takeZeros = Math.min(numZeros, k);
        k -= takeZeros;

        int takeNegOnes = Math.min(numNegOnes, k);
        sum -= takeNegOnes;

        return sum;
      
    }
}