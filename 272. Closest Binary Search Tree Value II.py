# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        diff = defaultdict()
        self.traverse(root, diff, target)
        return heapq.nsmallest(k, diff.keys(), key=diff.get)

    def closestKValues_quickselect(self, root: TreeNode, target: float, k: int) -> List[int]:
        # 1. Define a Traverse function:
        #     Traverse to get the array of all unique node's value
        #     and the hashmap of difference between itself and target
        # 2. Define a partition function:(left, right, array, diff)
        #     Choose one pivot randomly(we assume that it is the right most number of the array)
        #     Set one 'pointer' point to the position where pivot should be (before: the distance between this value and target is smaller than which between pivot and target; next: ...is larger than...)
        #     for i in range(left, right):
        #         if diff[array[i]] < diff[pivot]: exchange the places of pointer and array[i], pointer += 1
        #     exchange the places of pointer and pivot
        # 3. Define a select function:(left, right, array, diff, k)
        #     if pointer == k - 1: return array[:pointer]
        #     if pointer > k - 1: return select(left, pointer - 1, array, diff, k)
        #     if pointer < k - 1: return selcet(pointer + 1, right, array, diff, k)
        # TC -> O(N) on average, O(N^2) worst; Space -> O(N)
        diff = defaultdict()
        path = self.traverse(root, diff, target)
        return self.select(0, len(path) - 1, path, diff, k)

    def traverse(self, root, diff, target):
        if not root:
            return []
        diff[root.val] = abs(root.val - target)
        left = self.traverse(root.left, diff, target)
        right = self.traverse(root.right,  diff, target)
        return left + [root.val] + right

    def partition(self, left, right, path, diff):
        pivot = path[right]
        pointer = left

        for i in range(left, right):
            if diff[path[i]] < diff[pivot]:
                path[pointer], path[i] = path[i], path[pointer]
                pointer += 1
        path[pointer], path[right] = path[right], path[pointer]
        return pointer

    def select(self, left, right, path, diff, k):
        pointer = self.partition(left, right, path, diff)
        if pointer == k - 1:
            return path[:pointer + 1]
        if pointer > k-1:
            return self.select(left, pointer-1, path, diff, k)
        if pointer < k-1:
            return self.select(pointer + 1, right, path, diff, k)

    def closestKValues_twopointer(self, root: TreeNode, target: float, k: int) -> List[int]:
        # Get in-order traverse of the BST and find left and right in one path
        # Use a stack to iterate the BST, find the smallest one first
        # Move 'left' to left and 'right' to right to find k elements
        # TC: O(n+k); Space:O(n+h)

        stack, path, index, res = [], [], -1, []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            if node.right:
                n = node.right
                while n:
                    stack.append(n)
                    n = n.left
            if node.val < target:
                index += 1
            path.append(node.val)
        print(path, index)
        return self.get_k_elements(index, target, k, path, res)

    def get_k_elements(self, index, target, k, path, res):
        left, right = index, index + 1

        for _ in range(k):
            if right > len(path) - 1 or abs(path[left] - target) < abs(path[right] - target):
                res.append(path[left])
                left -= 1
            else:
                res.append(path[right])
                right += 1
        return res
