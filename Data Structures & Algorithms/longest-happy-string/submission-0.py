class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = []
        for val, key in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if not val:
                continue

            heapq.heappush(heap, (val, key))

        ans = ""
        while heap:
            val, key = heapq.heappop(heap)
            if len(ans) >= 2 and ans[-1] == ans[-2] == key:
                if not heap:
                    break
                    
                val1, key1 = heapq.heappop(heap)
                ans += key1
                val1 += 1

                if val1:
                    heapq.heappush(heap, (val1, key1))


            else:
                ans += key
                val += 1

            if val:
                heapq.heappush(heap, (val, key))

        return ans