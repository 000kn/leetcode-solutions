# 853. Car Fleet
# https://leetcode.com/problems/car-fleet/
# Difficulty: Medium
# Pattern: Sort by position (closest to target first), track arrival time,
# monotonic stack of fleet leaders — O(n log n)

class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)