class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = {i:i for i in range(n)}
        graph = defaultdict(list)
        rank = [1] * n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            
            return parent[x]

        def union(x, y):
            parentX = find(x)
            parentY = find(y)

            if parentX == parentY:
                return

            if rank[parentX] > rank[parentY]:
                parent[parentY] = parentX
                rank[parentX] += rank[parentY]

            else:
                parent[parentX] = parentY
                rank[parentY] += rank[parentX]


        for start, dest in edges:
            union(start, dest)

        seen = set()
        for i in range(n):
            rep = find(i)
            if rep not in seen:
                seen.add(rep)
        
        return len(seen)


