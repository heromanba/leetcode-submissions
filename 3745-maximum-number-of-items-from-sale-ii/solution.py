class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = float('-inf')
        min_price = float('inf')
        factor_map = dict()
        for i in range(len(items)):
            factor, price = items[i]
            max_factor = max(max_factor, factor)
            min_price = min(min_price, price)
            if factor not in factor_map:
                factor_map[factor] = [i]
            else:
                factor_map[factor].append(i)
        free_copy_list = []
        for i in range(len(items)):
            factor, price = items[i]
            if price // 2 < min_price:
                cnt = 0
                for multiple in range(factor, max_factor+1, factor):
                    if multiple in factor_map:
                        cnt += len(factor_map[multiple])
                free_copy_list.append((i, cnt-1)) # exclude self
        free_copy_list = sorted(free_copy_list, key=lambda x: (items[x[0]][1]))
        ans = 0
        # print(free_copy_list)
        for i, cnt in free_copy_list:
            factor, price = items[i]
            if budget >= price:
                buy_cnt = min(budget//price, cnt)
                budget -= buy_cnt*price
                ans += buy_cnt*2
                # print(i, buy_cnt, budget)
            else:
                break
        # print(budget)
        ans += (budget//min_price)
        return ans

