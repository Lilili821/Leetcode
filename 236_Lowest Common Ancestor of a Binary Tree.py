# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Divide and Conquer:
        # if left is None and right is None: return None
        # if left is not None and right is not None: return root
        # if root is p, return p
        # if root is q, return q
        # TC: O(N); Space: O(1)
        if not root:
            return None

        if root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None and right is None:
            return None
        if left is None:
            return right
        if right is None:
            return left

        return root
