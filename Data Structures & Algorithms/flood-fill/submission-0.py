class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(image), len(image[0])
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        start = image[sr][sc]
        stack = [[sr, sc]]
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        while stack:
            row, col = stack.pop()
            visited[row][col] = 1
            image[row][col] = color

            for r, c in directions:
                new_row = row + r
                new_col = col + c

                if inbound(new_row, new_col) and not visited[new_row][new_col] and image[new_row][new_col] == start:
                    stack.append([new_row, new_col])

        return image

