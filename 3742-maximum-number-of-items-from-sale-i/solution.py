import heapq
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        factor_map = dict()
        max_factor = float('-inf')
        min_price = float('inf')
        for i in range(len(items)):
            factor, price = items[i]
            if factor not in factor_map:
                factor_map[factor] = [i]
            else:
                factor_map[factor].append(i)
            max_factor = max(max_factor, factor)
            min_price = min(min_price, price)
        free_copy_list = []
        for i in range(len(items)):
            factor, price = items[i]
            cnt = 0
            for multiple in range(factor, max_factor+1, factor):
                if multiple in factor_map:
                    cnt += len(factor_map[multiple])
            avg_price = price / cnt
            if avg_price < min_price and price <= budget:
                free_copy_list.append((i, cnt))

        if len(free_copy_list) == 0:
            return budget // min_price

        dp = [
            [-1 for _ in range(budget+1)]
            for _ in range(len(free_copy_list)+1)
        ]
        dp[0][0] = 0
        # print(free_copy_list)
        for i in range(1, len(free_copy_list)+1):
            idx, cnt = free_copy_list[i-1]
            factor, price = items[idx]
            for spent in range(budget+1):
                # skip current
                dp[i][spent] = dp[i-1][spent]
                if spent >= price and dp[i-1][spent-price] != -1:
                    dp[i][spent] = max(dp[i][spent], dp[i-1][spent-price]+cnt)
                # include current
        # for row in dp:
        #     print(row)
        max_cnt = 0
        min_spent = 0
        for spent in range(budget, -1, -1):
            curr_cnt = dp[-1][spent] + (budget-spent)//min_price
            if curr_cnt >= max_cnt:
                max_cnt = curr_cnt
        # print(min_spent, max_cnt)
        return max_cnt
