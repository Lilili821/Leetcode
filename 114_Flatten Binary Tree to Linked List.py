# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: "TreeNode") -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Divide and Conquer
        # Each time, return the last node
        # 1. root is None: return None
        # 2. left is None and right is None: return root
        # 3. One of them is not None: return the other one's last node
        #   make sure they are all in the right side of the root.
        # 4. Both not None:
        #   left_lastnode.right = root.right
        #   root.right = root.left
        #   root.left = None
        #   TC: O(N); Space: O(1)

        self.flatten_divide(root)

    def flatten_divide(self, root):
        if not root:
            return None

        left_last = self.flatten_divide(root.left)
        right_last = self.flatten_divide(root.right)

        if not left_last and not right_last:
            return root
        if not left_last:
            return right_last
        if not right_last:
            root.right = root.left
            root.left = None
            return left_last
        left_last.right = root.right
        root.right = root.left
        root.left = None
        return right_last
