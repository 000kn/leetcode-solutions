# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
# Difficulty: Medium
# Pattern: Monotonic stack — stack holds indices with decreasing temps, pop when a warmer day is found — O(n)

class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer