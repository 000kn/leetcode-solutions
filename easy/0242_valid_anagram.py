# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Pattern: Hash map — count characters in both strings, compare counts — O(n)

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT