# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Difficulty: Medium
# Pattern: Binary Search — compare nums[mid] to nums[r]; use r = mid (not mid-1)
# and while l < r to avoid overwriting the answer when mid == r — O(log n)

class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]