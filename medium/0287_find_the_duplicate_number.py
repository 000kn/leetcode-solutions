# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/
# Difficulty: Medium
# Pattern: Floyd's Cycle Detection (fast/slow pointers), array-as-linked-list

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow