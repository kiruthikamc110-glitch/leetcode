# Last updated: 14/07/2026, 14:56:44
class Solution(object):
    def splitMessage(self, message, limit):
        """
        :type message: str
        :type limit: int
        :rtype: List[str]
        """
        n = len(message)
        
        # Enumerate the number of digits that total parts 'b' can have
        for len_b in range(1, 6):
            # Calculate total message capacity available for all parts if total parts is 'b'
            # We can find the exact 'b' by iterating or calculating
            # Let's check potential values of b within this digit length scope
            low = 10**(len_b - 1)
            high = 10**len_b - 1
            
            # Auxiliary tracking for capacity calculation
            # To avoid recalculating from scratch, we can compute total capacity iteratively
            # components of suffix: '<', '/', '>' contribute 3 characters
            # plus len(b) contributed by the denominator
            fixed_suffix_len = 3 + len_b 
            
            # Calculate total capacity up to the start of this digit range
            # combined with our search loop
            total_capacity = 0
            # Pre-populate capacity from previous ranges
            for prev_len in range(1, len_b):
                count = 9 * (10**(prev_len - 1))
                total_capacity += count * (limit - (prev_len + fixed_suffix_len))
            
            for b in range(low, high + 1):
                # Add capacity for the current part 'b'
                current_a_len = len(str(b))
                available_space = limit - (current_a_len + fixed_suffix_len)
                
                # If a single suffix exceeds or equals the limit, it's impossible for this limit
                if available_space <= 0:
                    break
                    
                total_capacity += available_space
                
                # If we have enough capacity to hold the entire message
                if total_capacity >= n:
                    # Construct and return the split parts
                    ans = []
                    idx = 0
                    for a in range(1, b + 1):
                        suffix = "<" + str(a) + "/" + str(b) + ">"
                        cap = limit - len(suffix)
                        ans.append(message[idx : idx + cap] + suffix)
                        idx += cap
                    return ans
                    
        return []