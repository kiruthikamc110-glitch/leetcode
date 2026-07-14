// Last updated: 14/07/2026, 14:57:11
import java.util.*;

class Solution {
    // Helper class to store a node along with its row and column coordinates
    private static class Point implements Comparable<Point> {
        int row;
        int col;
        int val;

        Point(int row, int col, int val) {
            this.row = row;
            this.col = col;
            this.val = val;
        }

        @Override
        public int compareTo(Point other) {
            // 1. First sort by column from left to right
            if (this.col != other.col) {
                return Integer.compare(this.col, other.col);
            }
            // 2. If columns are identical, sort by row from top to bottom
            if (this.row != other.row) {
                return Integer.compare(this.row, other.row);
            }
            // 3. If both row and column are identical, sort by node value ascending
            return Integer.compare(this.val, other.val);
        }
    }

    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        List<Point> points = new ArrayList<>();
        // DFS traversal to collect all nodes with their coordinates
        dfs(root, 0, 0, points);

        // Sort all coordinates according to the problem description rules
        Collections.sort(points);

        // Group sorted points into lists by column index
        int i = 0;
        while (i < points.size()) {
            List<Integer> currentColumn = new ArrayList<>();
            int colIndex = points.get(i).col;

            // Collect all values belonging to the same column
            while (i < points.size() && points.get(i).col == colIndex) {
                currentColumn.add(points.get(i).val);
                i++;
            }
            result.add(currentColumn);
        }

        return result;
    }

    private void dfs(TreeNode node, int row, int col, List<Point> points) {
        if (node == null) {
            return;
        }
        
        points.add(new Point(row, col, node.val));
        dfs(node.left, row + 1, col - 1, points);
        dfs(node.right, row + 1, col + 1, points);
    }
}