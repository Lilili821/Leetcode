# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:
    # Use a stack to store nodes; if it is not empty, then it has Next
    # Initialize: get all left nodes until the last left one(smallest)
    # next: get the node then simply pop it.
    # if the node has right, right.left is not None, then the next should be the smallest left
    # TC -> O(N); Space -> O(h)

    def __init__(self, root: "TreeNode"):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack[-1]
        self.stack.pop()
        if node.right:
            n = node.right
            while n:
                self.stack.append(n)
                n = n.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
