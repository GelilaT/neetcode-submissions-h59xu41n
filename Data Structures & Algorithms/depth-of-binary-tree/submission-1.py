# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(root, dep):

            nonlocal ans
            if not root.left and not root.right:
                ans = max(ans, dep)
                return 

            if root.left:
                dfs(root.left, dep + 1)

            if root.right:
                dfs(root.right, dep + 1)

        if not root:
            return ans

        dfs(root, 1)
        return ans