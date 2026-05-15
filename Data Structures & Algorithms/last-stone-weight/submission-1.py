class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            val1 = -heapq.heappop(heap)
            val2 = -heapq.heappop(heap)

            if val1 == val2:
                continue

            diff = val1 - val2
            heapq.heappush(heap, -diff)

        return -heap[0] if heap else 0

        
        