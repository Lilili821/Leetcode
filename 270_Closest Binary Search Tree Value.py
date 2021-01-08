# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root: "TreeNode", target: float) -> int:
        # Use 'left' and 'right' two variables to represent the node smaller than target and another one greater than target
        # Traverse from the root:
        #     while root:
        #     if root.val > target: right = root.val; root = root.left
        #     if root.val < target: left = root.val; root = root.right
        # TC: O(h); Space: O(1)
        left, right = root.val, root.val
        while root:
            if root.val > target:
                right = root.val
                root = root.left
            else:
                left = root.val
                root = root.right

        if abs(target-left) > abs(right - target):
            return right
        return left
