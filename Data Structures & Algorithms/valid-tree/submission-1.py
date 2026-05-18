class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for start, dest in edges:
            graph[start].append(dest)
            graph[dest].append(start)

        visited = [0] * n
        def dfs(node, par):

            visited[node] = 1
            for nei in graph[node]:
                
                if nei == par:
                    continue

                if visited[nei] == 1:
                    return False

                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and sum(visited) == n


        