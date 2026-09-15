class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for idx, [x, y] in enumerate(points):
            dist = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(heap, [dist, idx])

        ans = []
        for _ in range(k):
            idx = heapq.heappop(heap)[1]
            ans.append(points[idx])

        return ans



        