// Last updated: 14/07/2026, 15:27:40
class Solution {
    private int minDiff = Integer.MAX_VALUE;
    private TreeNode prev = null;

    public int getMinimumDifference(TreeNode root) {
        inorder(root);
        return minDiff;
    }
    private void inorder(TreeNode root) {
        if (root == null) {
            return;
        }
        inorder(root.left);
        if (prev != null) {
            minDiff = Math.min(minDiff, root.val - prev.val);
        }
        prev = root;
        inorder(root.right);
    }
}