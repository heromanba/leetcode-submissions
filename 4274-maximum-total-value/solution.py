class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        MOD = 10**9 + 7
        n = len(value)
        
        # 1. Helper function to count operations for a given threshold X
        def count_ops(X):
            total_ops = 0
            for v, d in zip(value, decay):
                if v < X:
                    continue
                if d == 0:
                    # If decay is 0 and value >= X, it can provide infinite elements
                    return float('inf')
                # Max t such that v - d * (t - 1) >= X
                t = (v - X) // d + 1
                total_ops += t
            return total_ops

        # 2. Binary search for the exact threshold
        low, high = 0, max(value)
        threshold = 0
        
        while low <= high:
            mid = (low + high) // 2
            if count_ops(mid) >= m:
                threshold = mid
                low = mid + 1
            else:
                high = mid - 1
                
        # 3. Collect all values strictly greater than our threshold
        ans = 0
        elements_used = 0
        
        for v, d in zip(value, decay):
            if v <= threshold:
                continue
            
            # Count elements that are strictly > threshold
            if d == 0:
                # If decay is 0, we can take as many as needed up to m
                k = m - elements_used
            else:
                k = (v - (threshold + 1)) // d + 1
            
            # Bound k by the remaining allowed moves
            k = min(k, m - elements_used)
            
            if k > 0:
                # Sum of Arithmetic Progression: k * v - d * k * (k - 1) // 2
                current_sum = k * v - d * k * (k - 1) // 2
                ans = (ans + current_sum) % MOD
                elements_used += k

        # 4. Fill the remaining slots with the threshold value itself
        if elements_used < m:
            remaining = m - elements_used
            ans = (ans + remaining * threshold) % MOD
            
        return ans

