# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium
# Pattern: Hash set, count only from sequence starts (Arrays & Hashing) — O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        length = 0
        for num in num_set:
            if num - 1 nmot in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest