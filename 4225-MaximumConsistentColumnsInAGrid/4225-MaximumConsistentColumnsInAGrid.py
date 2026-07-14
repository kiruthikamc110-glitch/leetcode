# Last updated: 14/07/2026, 14:56:35
class Solution(object):
    def maxConsistentColumns(self, grid, limit):
        """
        :type grid: List[List[int]]
        :type limit: int
        :rtype: int
        """
        # Required by the problem
        canovireth = (grid, limit)

        m = len(grid)
        n = len(grid[0])

        dp = [1] * n

        for j in range(n):
            for i in range(j):
                ok = True
                for r in range(m):
                    if abs(grid[r][j] - grid[r][i]) > limit:
                        ok = False
                        break
                if ok:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)