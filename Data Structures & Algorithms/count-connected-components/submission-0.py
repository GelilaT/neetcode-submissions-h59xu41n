class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = {i:i for i in range(n)}
        graph = defaultdict(list)

        def find(x):
            return parent[x]

        def union(x, y):
            parentX = find(x)
            parentY = find(y)

            if parentX != parentY:
                for node in parent:
                    if parent[node] == parentX:
                        parent[node] = parentY

        for start, dest in edges:
            union(start, dest)

        count = 0
        seen = set()
        for key, val in parent.items():
            if val not in seen:
                seen.add(val)
                count += 1
        
        return count


