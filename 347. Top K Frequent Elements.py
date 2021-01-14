class Solution:
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        # Traverse the nums list and get a hashmap of each unique number's frequency
        # Use heapq.nlargest to get the k most frequent elements
        # TC -> O(N + NlogK) -> O(NlogK); Space -> O(k+N)
        freq_count = Counter(nums)
        return heapq.nlargest(k, freq_count.keys(), key=freq_count.get)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use Counter to get a hashmap of each unique number's frequency
        # Quick Select for the number array based on number's frequency:
            # 1. define a partition function:
            #     randomly choose a pivot (assume the right one), then use one pointer points to the pos where pivot should be
            #     for i in range(left, right):
            #         if counter[nums[i]] < counter[pivot]: nums[pointer] and nums[i] exchange their places
            #     After the loop, exchang places of pointer and pivot
            # 2. define a select function:(left, right, counter, unqiues)
            #     pointer = self.partition(left, right, counter, uniques)
            #     if len(couter.keys()) - pointer == k:  return uniques[pointer:]
            #     if ............................ < k: return select(left, pointer -1, counter, uniques)
            #     if ............................ > k: return select(pointer + 1, right, counter, uniques)
            # TC -> O(N) average, O(N^2) the worst-case; Space -> O(N)
        freq_count = Counter(nums)
        uniques = list(freq_count.keys())
        left, right = 0, len(uniques) - 1
        return self.select(left, right, uniques, freq_count, k)

    def partition(self, left, right,  uniques, freq_count):
        pivot = uniques[right]
        pointer = left
        for i in range(left, right):
            if freq_count[uniques[i]] < freq_count[pivot]:
                uniques[i], uniques[pointer] = uniques[pointer], uniques[i]
                pointer += 1
        uniques[pointer], uniques[right] = uniques[right], uniques[pointer]
        return pointer

    def select(self, left, right, uniques, freq_count, k):
        pointer = self.partition(left, right, uniques, freq_count)
        if len(uniques) - pointer == k:
            return uniques[pointer:]
        if len(uniques) - pointer < k:
            return self.select(left, pointer - 1, uniques, freq_count, k)
        if len(uniques) - pointer > k:
            return self.select(pointer + 1, right, uniques, freq_count, k)
