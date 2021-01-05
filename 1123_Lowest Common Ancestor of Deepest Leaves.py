# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: 'TreeNode') -> 'TreeNode':
        # 1. Define a function get_lca; return (lca, depth)
        # 2. If left_depth > right_depth, return lca_left, left_depth + 1
        #   If left_depth < right_depth, return lca_right, right_depth + 1
        #   If left_depth == right_depth, return root, depth + 1
        # TC: O(N); Space: O(1)
        res = self.get_lca(root)
        return res[0]

    def get_lca(self, root):
        if not root:
            return (None, 0)

        left_lca, left_depth = self.get_lca(root.left)
        right_lca, right_depth = self.get_lca(root.right)

        if left_depth > right_depth:
            return (left_lca, left_depth + 1)
        if left_depth < right_depth:
            return (right_lca, right_depth + 1)
        return (root, left_depth + 1)
