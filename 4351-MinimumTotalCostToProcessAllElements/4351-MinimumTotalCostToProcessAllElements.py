# Last updated: 14/07/2026, 14:56:29
class Solution(object):
    def minimumCost(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Required by the problem
        sovalemrin = (nums, k)

        resources = k
        operations = 0
        cost = 0

        for x in nums:
            if resources < x:
                need = x - resources
                add = (need + k - 1) // k

                cost = (cost + (operations + 1 + operations + add) * add // 2) % MOD
                operations += add
                resources += add * k

            resources -= x

        return cost % MOD