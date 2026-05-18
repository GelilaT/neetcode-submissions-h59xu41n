class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        incoming = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        queue = deque()
        for idx, val in enumerate(incoming):
            if val == 0:
                queue.append(idx)

        order = []
        while queue:
            
            course = queue.popleft()
            order.append(course)
            for nei in graph[course]:

                incoming[nei] -= 1
                if incoming[nei] == 0:
                    queue.append(nei)

        if len(order) != numCourses:
            return []

        return order
