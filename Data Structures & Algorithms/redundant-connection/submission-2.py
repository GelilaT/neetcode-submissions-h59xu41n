class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        rep = {i:i for i in range(1, n + 1)}
        def find(x):
            if x == rep[x]:
                return x

            rep[x] = find(rep[x])
            return rep[x]

        for x, y in edges:
            repX, repY = find(x), find(y)
            if repX == repY:
                return [x, y]

            rep[repX] = repY
