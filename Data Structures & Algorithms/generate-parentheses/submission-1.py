class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        def backtrack(left, right, path):
            
            if len(path) == 2 * n:
                ans.append("".join(path))
                return

            if left < n:
                path.append("(")
                backtrack(left + 1, right, path)
                path.pop()

            if right < left:
                path.append(")")
                backtrack(left, right + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return ans
        

        