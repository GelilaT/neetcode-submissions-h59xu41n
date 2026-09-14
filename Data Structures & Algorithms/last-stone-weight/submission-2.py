class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) >= 2:

            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first == second:
                continue

            heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0
