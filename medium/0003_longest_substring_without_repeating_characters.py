# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Pattern: Sliding Window — expand right pointer, shrink left pointer when
# duplicate found, track max window size using a set — O(n)

class Solution:
    def lengthOfLongestSubstring(self, s):
        l = 0
        charset = set()
        res = 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r - l + 1)
        return res