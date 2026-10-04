class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()
        for idx, degree in enumerate(indegree):
            if degree == 0:
                q.append(idx)

        courses = 0
        while q:

            cur = q.popleft()
            courses += 1
            for nei in graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return courses == numCourses

