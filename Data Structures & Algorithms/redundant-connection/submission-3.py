class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        rep = {i:i for i in range(1, n + 1)}
        rank = [1] * (n + 1)
        def find(x):
            if x != rep[x]:
                rep[x] = find(rep[x])
            return rep[x]

        def union(n1, n2):
            
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                rep[p2] = p1
                rank[p1] += rank[p2]
            else:
                rep[p1] = p2
                rank[p2] += rank[p1]

            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]