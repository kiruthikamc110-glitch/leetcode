# Last updated: 14/07/2026, 14:57:09
from collections import Counter

class Solution(object):
    def gridIllumination(self, n, lamps, queries):
        """
        :type n: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Counters to track how many lamps illuminate a specific line
        rows = Counter()
        cols = Counter()
        diag1 = Counter()  # r - c
        diag2 = Counter()  # r + c
        
        # Set to track the exact positions of active unique lamps
        active_lamps = set()
        
        for r, c in lamps:
            if (r, c) not in active_lamps:
                active_lamps.add((r, c))
                rows[r] += 1
                cols[c] += 1
                diag1[r - c] += 1
                diag2[r + c] += 1
                
        ans = []
        
        for r, c in queries:
            # 1. Check if the current cell is illuminated
            if rows[r] > 0 or cols[c] > 0 or diag1[r - c] > 0 or diag2[r + c] > 0:
                ans.append(1)
            else:
                ans.append(0)
                
            # 2. Check the cell and its 8 adjacent neighbors to turn off lamps
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    
                    if (nr, nc) in active_lamps:
                        # Turn off the lamp
                        active_lamps.remove((nr, nc))
                        rows[nr] -= 1
                        cols[nc] -= 1
                        diag1[nr - nc] -= 1
                        diag2[nr + nc] -= 1
                        
        return ans