import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heaps = nums
        heapq.heapify(self.heaps)

        while len(self.heaps) > k:
            heapq.heappop(self.heaps)

    def add(self, val: int) -> int:
        heapq.heappush(self.heaps, val)

        if len(self.heaps) > self.k:
            heapq.heappop(self.heaps)

        return self.heaps[0]


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4,5,8,2])

result = []
result.append(obj.add(3))
result.append(obj.add(5))
result.append(obj.add(10))
result.append(obj.add(9))
result.append(obj.add(4))

print(result)
