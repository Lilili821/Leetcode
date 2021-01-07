"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # 1. If the node has right:
        #     then the successor should be the node.right's last left till we can (If there is node.right's left, otherwise it should be node.right)
        # 2. If the node does not have right:
        #     if node.parent.left = node, the successor should be the parent
        #     if not, keep find parent's parent unitl the ancestor's left = one of the parent or parent is None, which means not found, then return None
        # TC: O(h) h means the depth of the tree, Space:O(1)
        res = None
        if node.right:
            n = node.right
            while n:
                res = n
                n = n.left
        else:
            n = node.parent
            m = node
            while n:
                if n.left is m:
                    res = n
                    break
                m = n
                n = n.parent

        return res
