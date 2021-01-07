# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:
    # Get one stack to finish the iterator, which is mainly for next
    # Creat one path(list) to store the whole path (ascending), and one pointer to represent the current position.
    # if we want to get previous one, just need to move the pointer, no need to change the iterator stack
    # For 'next' after 'prev', also move the pointer, instead of changing the stack
    # TC: O(N+k); Space: O(N)
    def __init__(self, root: "TreeNode"):
        self.stack_next = []
        self.path = []
        self.pointer = -1
        while root:
            self.stack_next.append(root)
            root = root.left

    def hasNext(self) -> bool:
        return len(self.stack_next) > 0 or self.pointer < len(self.path) - 1

    def next(self) -> int:
        if self.pointer < len(self.path) - 1:
            self.pointer += 1
            return self.path[self.pointer].val
        node = self.stack_next[-1]
        self.stack_next.pop()
        if node.right:
            n = node.right
            while n:
                self.stack_next.append(n)
                n = n.left
        self.path.append(node)
        self.pointer += 1
        return node.val

    def hasPrev(self) -> bool:
        return self.pointer > 0

    def prev(self) -> int:
        self.pointer -= 1
        node = self.path[self.pointer]
        return node.val


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()
