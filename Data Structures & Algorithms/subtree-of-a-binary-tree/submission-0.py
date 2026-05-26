# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):

            if not p and not q:
                return True

            if p and q and q.val == p.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)

            return False

        res = False
        curr = root
        while root or curr:
            if root:
                if root.val and subRoot.val:
                    res = res or sameTree(root, subRoot)
                root = root.left

            if curr:
                if curr.val and subRoot.val:
                    res = res or sameTree(curr, subRoot)
                curr = curr.right


        return res
            


        



        