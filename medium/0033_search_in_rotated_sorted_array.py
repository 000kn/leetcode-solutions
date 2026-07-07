# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium
# Pattern: Binary Search — determine which half is sorted, then check if target
# falls within that sorted range to decide direction — O(log n)

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1