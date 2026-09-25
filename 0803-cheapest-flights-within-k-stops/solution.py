import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for u, v, w in flights:
            if u not in graph:
                graph[u] = [(v, w)]
            else:
                graph[u].append((v, w))
        if src not in graph:
            return -1
        prices = [[float('inf')]*(k+1) for _ in range(n)]
        # (price, node, n_stops)
        pq = [(0, src, 0)]
        while pq:
            price, node, n_stops = heapq.heappop(pq)
            if node not in graph:
                continue
            if n_stops > k:
                continue
            for adj, adj_price in graph[node]:
                # print(adj, n_stops, price, adj_price, prices[adj][n_stops])
                if price+adj_price < prices[adj][n_stops]:
                    prices[adj][n_stops] = price+adj_price
                    heapq.heappush(pq, (price+adj_price, adj, n_stops+1))
        # print(prices[dst])
        min_price = min(prices[dst])
        return -1 if min_price == float('inf') else min_price
