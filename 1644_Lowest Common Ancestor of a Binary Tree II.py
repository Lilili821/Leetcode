# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # use boolean lca present find the LCA or not, every time return (node, lca)
        # if left = (node_l, False), right = (node_r, False), return (root, True)
        # if left = (None, False), right = (Nonde, False), return (None, False)
        # if root is p or q:
        #     if left is None and right is None, return (root, False);
        #     else return (root, True)
        # TC: O(N), Space:O(1)
        res = self.find_LCA(root, p, q)
        if not res[1]:
            return None
        return res[0]

    def find_LCA(self, root, p, q):
        if not root:
            return (None, False)

        left = self.find_LCA(root.left, p, q)
        right = self.find_LCA(root.right, p, q)

        if root is p or root is q:
            if not left[0] and not right[0]:
                return (root, False)
            return (root, True)

        if not left[0] and not right[0]:
            return (None, False)
        if not left[0]:
            return right
        if not right[0]:
            return left
        return (root, True)
