# 703. Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Difficulty: Easy
# Pattern: Min-heap of fixed size k (top of heap = kth largest)

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minH = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.minH) < self.k:
            heapq.heappush(self.minH, val)
        elif val > self.minH[0]:
            heapq.heappop(self.minH)
            heapq.heappush(self.minH, val)

        return self.minH[0]