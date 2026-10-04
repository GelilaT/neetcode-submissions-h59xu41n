class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        incoming = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        q = deque()
        for idx, val in enumerate(incoming):
            if val == 0:
                q.append(idx)

        courses = []
        while q:

            cur = q.popleft()
            courses.append(cur)
            for nei in graph[cur]:
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    q.append(nei)

        return courses if len(courses) == numCourses else []
        
