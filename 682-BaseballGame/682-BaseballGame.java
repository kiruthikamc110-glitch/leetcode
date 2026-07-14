// Last updated: 14/07/2026, 15:27:14
class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> scoreRecord = new Stack<>();
        
        for (String op : operations) {
            if (op.equals("C")) {
                // Remove the last score
                scoreRecord.pop();
            } else if (op.equals("D")) {
                // Record double the previous score
                scoreRecord.push(2 * scoreRecord.peek());
            } else if (op.equals("+")) {
                // Record the sum of the previous two scores
                int top = scoreRecord.pop();
                int nextToTop = scoreRecord.peek();
                int sum = top + nextToTop;
                
                // Put the removed top back, then add the new sum
                scoreRecord.push(top);
                scoreRecord.push(sum);
            } else {
                // It's an integer, parse and record it
                scoreRecord.push(Integer.parseInt(op));
            }
        }
        
        // Sum all elements remaining in the stack
        int totalSum = 0;
        for (int score : scoreRecord) {
            totalSum += score;
        }
        
        return totalSum;
    }
}  