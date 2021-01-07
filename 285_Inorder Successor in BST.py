# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # First think about recursion to get a whole path then iterate the whole path to find p and its next; But it is a two path way, TC should be 2N
        # To find the node one by one, we should think about iterator the BST
        # Use a stack to finish the iteration, first get the smallest one, then iterate one by one until find p. The last element in the stack should be the inorder successor
        # TC: O(N); Space: O(h)

        stack = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack[-1]
            stack.pop()
            if node.right:
                n = node.right
                while n:
                    stack.append(n)
                    n = n.left

            if node is p and len(stack) > 0:
                return stack[-1]

        return None
