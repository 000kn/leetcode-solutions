# 78. Subsets
# https://leetcode.com/problems/subsets/
# Difficulty: Medium
# Pattern: Backtracking - include/exclude decision tree

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_subset = []

        def backtrack(index):
            if index == len(nums):
                res.append(curr_subset[:])
                return

            curr_subset.append(nums[index])
            backtrack(index + 1)

            curr_subset.pop()
            backtrack(index + 1)

        backtrack(0)
        return res