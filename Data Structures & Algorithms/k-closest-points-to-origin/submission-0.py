class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distance = []
        for i, point in enumerate(points):
            x, y = point
            dist = x**2 + y**2
            heapq.heappush(distance, (dist, i))

        ans = []
        for _ in range(k):
            dist, idx = heapq.heappop(distance)
            ans.append(points[idx])

        return ans



        