import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)
            print(heap)
        return [i[1] for i in heap]

obj = Solution()
print(obj.topKFrequent([1,1,1,2,2,3], 2))