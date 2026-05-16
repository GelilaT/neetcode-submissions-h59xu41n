class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        def dfs(cur, left, right):

            if left + right == 2 * n:
                ans.append("".join(cur))
                return

            if left < n:
                cur.append("(")
                dfs(cur, left + 1, right)
                cur.pop()

            if right < left:
                cur.append(")")
                dfs(cur, left, right + 1)
                cur.pop()

        dfs([], 0, 0)
        return ans


        