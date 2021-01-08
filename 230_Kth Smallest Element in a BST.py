# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: "TreeNode", k: int) -> int:
        # Iterate the BST one by one to get the in-order traversal until find the kth smallest
        # Iterator:
        #     First find the far left node (which is the smallest one)
        #     Use a stack to store nodes waiting to be processed
        #     Find the next element:
        #         1. If right:
        #             pop the node out from the stack
        #             get right node's far left subtree node
        #         2. If not right:
        #             just pop this node out
        # TC: O(h+k) -> Use O(h) to find the smallest one and use k to find the kth element
        # Space: O(h) -> there will be at most h elements in the stack
        stack = []
        while root:
            stack.append(root)
            root = root.left
        for _ in range(k):
            res = self.iterate_BST(stack)

        return res.val

    def iterate_BST(self, stack):
        node = stack.pop()
        if node.right:
            n = node.right
            while n:
                stack.append(n)
                n = n.left
        return node
