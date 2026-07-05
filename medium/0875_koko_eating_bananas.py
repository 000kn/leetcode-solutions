import math

# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/
# Difficulty: Medium
# Pattern: Binary Search on answer space — search over possible speeds k,
# check feasibility with total hours needed — O(n log(max(piles)))

class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / mid)
            if total_time <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res