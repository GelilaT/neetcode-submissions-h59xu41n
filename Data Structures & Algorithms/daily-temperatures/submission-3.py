class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            if not stack:
                ans[i] = 0
                stack.append([temperatures[i], i])

            else:
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()

                if stack:
                    ans[i] = stack[-1][1] - i

                else:
                    ans[i] = 0

                stack.append([temperatures[i], i])

        return ans


