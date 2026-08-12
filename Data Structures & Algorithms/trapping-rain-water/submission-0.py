class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        maxArea = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                popped = stack.pop()
                if stack:
                    left = height[stack[-1]]
                    right = h
                    mid = height[popped]
                    area = (min(right, left) - mid) * (i - stack[-1] - 1)
                    maxArea += area

            stack.append(i)

        return maxArea


        