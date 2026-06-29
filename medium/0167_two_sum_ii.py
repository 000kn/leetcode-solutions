# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Difficulty: Medium
# Pattern: Two Pointers

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            currentSum = numbers[l] + numbers[r]

            if currentSum > target:
                r -= 1
            elif currentSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []