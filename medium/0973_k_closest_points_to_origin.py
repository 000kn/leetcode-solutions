# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# Difficulty: Medium
# Pattern: Min-heap of (distance, x, y) tuples, pop k times

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = [(x**2 + y**2, x, y) for x, y in points]
        heapq.heapify(minH)

        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(minH)
            res.append([x, y])

        return res