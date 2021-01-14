# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: "TreeNode") -> bool:
        # Iterator the node one by one use the stack;
        # Get next:
        #   If the node has right: go to the right's left most node
        #   If not: pop the next element in the stack
        # Set two variables 'prev' and 'cur':
        #     At first, 'prev' is equal to the left most node, cur is the next one in the in-order traverse element
        #     If 'cur' > 'prev', return False
        # return True
        # TC -> O(N); Space -> O(1)
        stack = []
        while root:
            stack.append(root)
            root = root.left

        prev = stack[-1].val - 1
        while stack:
            node = stack.pop()
            if node.right:
                n = node.right
                while n:
                    stack.append(n)
                    n = n.left
            cur = node.val
            if cur <= prev:
                return False
            prev = cur

        return True
