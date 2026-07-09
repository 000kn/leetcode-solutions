# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Difficulty: Medium
# Pattern: Sliding Window — track char counts + max frequency in window,
# shrink when (window size - maxFreq) > k — O(n)

class Solution:
    def characterReplacement(self, s, k):
        count = {}
        l = 0
        maxFreq = 0
        res = 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])
            if (r - l + 1) - maxFreq <= k:
                res = max(res, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
        return res