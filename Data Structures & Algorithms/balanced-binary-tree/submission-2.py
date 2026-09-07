# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ans = 0
        def dfs(root):

            nonlocal ans
            if not root:
                return 0

            left = dfs(root.left) 
            right = dfs(root.right) 
            if abs(left - right) > 1:
                ans += 1

            return 1 + max(left, right)

        dfs(root)
        print(ans)
        return False if ans else True
        
        