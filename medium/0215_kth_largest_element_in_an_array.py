# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Difficulty: Medium
# Pattern: Min-heap of fixed size k (top of heap = kth largest)

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minH = []

        for num in nums:
            if len(minH) < k:
                heapq.heappush(minH, num)
            elif num > minH[0]:
                heapq.heappop(minH)
                heapq.heappush(minH, num)

        return minH[0]