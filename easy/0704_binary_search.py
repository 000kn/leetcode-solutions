# 704. Binary Search
# https://leetcode.com/problems/binary-search/
# Difficulty: Easy
# Pattern: Binary Search — halve the search space each step by comparing target to nums[mid] — O(log n)

class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1