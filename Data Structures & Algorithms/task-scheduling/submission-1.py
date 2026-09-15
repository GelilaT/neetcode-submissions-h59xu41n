class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        heap = []
        for count in count.values():
            heapq.heappush(heap, -count)

        q = deque()
        time = 0
        while q or heap:

            time += 1
            if not heap:
                time = q[0][1]
            
            else:
                cur = 1 + heapq.heappop(heap)
                if cur != 0:
                    q.append([cur, time + n])

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time

            

        