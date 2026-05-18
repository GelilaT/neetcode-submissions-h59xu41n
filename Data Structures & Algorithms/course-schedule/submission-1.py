class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        incoming = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        q = deque()
        for idx, val in enumerate(incoming):
            if val == 0:
                q.append(idx)

        courses = 0
        while q:
            cour = q.popleft()
            courses += 1

            for nei in graph[cour]:
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    q.append(nei)

        print(courses)
        return courses == numCourses
