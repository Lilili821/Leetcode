import heapq


class Solution:

    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        # Heap, return heapq.nlargest(k, nums)[-1]
        # Space -> O(N)
        heapq.heapify(nums)  # TC -> O(N)
        for _ in range(len(nums)-k+1):
            res = heapq.heappop(nums)  # TC -> O((len(nums)-k+1)logN)
        return res

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quick Select:
        # 1. Choose one pivot randomly
        # 2. Put all elements smaller that it to its left and larger or equal elements to right
        # 3. Compare pivot's postion with N-k, choose the side of array to recursively proceed
        # TC -> Average: O(N); Worst: O(N^2)
        left, right = 0, len(nums) - 1
        k_smallest = len(nums) - k
        return self.select(left, right, nums, k_smallest)

    def partition(self, left, right, nums):
        pivot = nums[right]
        pointer = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1

        nums[pointer], nums[right] = nums[right], nums[pointer]
        return pointer

    def select(self, left, right, nums, k):
        pointer = self.partition(left, right, nums)
        if pointer == k:
            return nums[pointer]
        if pointer < k:
            return self.select(pointer + 1, right, nums, k)
        if pointer > k:
            return self.select(left, pointer - 1, nums, k)
