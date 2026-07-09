# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/
# Difficulty: Medium
# Pattern: Fixed-size sliding window — build initial window count, then
# slide by adding new char and removing oldest, compare counts — O(n)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = {}
        for i in range(len(s1)):
            if s1[i] not in count1:
                count1[s1[i]] = 0
            count1[s1[i]] += 1

        count2 = {}
        for i in range(len(s1)):
            if s2[i] not in count2:
                count2[s2[i]] = 0
            count2[s2[i]] += 1

        if count1 == count2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            if s2[r] not in count2:
                count2[s2[r]] = 0
            count2[s2[r]] += 1
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]
            l += 1
            if count1 == count2:
                return True
        return False