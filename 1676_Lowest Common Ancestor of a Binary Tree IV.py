# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # The same as the origin one
        # if root in nodes: return root
        # if left and right is None: return None
        # if left is None or right is None: return the other one
        # if left and right: return root
        # TC: O(N); Space: O(1)
        nodes = set(nodes)
        if not root:
            return None

        if root in nodes:
            return root

        left = self.lowestCommonAncestor(root.left, nodes)
        right = self.lowestCommonAncestor(root.right, nodes)

        if not left and not right:
            return None
        if not left:
            return right
        if not right:
            return left
        return root
