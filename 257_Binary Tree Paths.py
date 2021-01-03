# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        # 1. Divide and Conquer:
        # For each node, its paths = (node + each path in left subtree) + (node + each path in right subtree)
        # TC: O(N); Space: O()
        # paths = self.get_path(root)
        # return paths

        # 2. DFS:
        # When reaching to a leaf, list result append the current path
        # TC: O(N); Space:O()
        if not root:
            return []
        result = []
        self.dfs(root, [str(root.val)], result)
        return result

    def get_path(self, root):
        if not root:
            return []

        left_paths = self.get_path(root.left)
        right_paths = self.get_path(root.right)

        if not left_paths and not right_paths:
            return [str(root.val)]

        paths = []
        for path in left_paths + right_paths:
            paths.append(str(root.val) + '->' + path)

        return paths

    def dfs(self, root, path, result):
        if not root.left and not root.right:
            result.append('->'.join(path))

        if root.left:
            path.append(str(root.left.val))
            self.dfs(root.left, path, result)
            path.pop()

        if root.right:
            path.append(str(root.right.val))
            self.dfs(root.right, path, result)
            path.pop()
