# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# Difficulty: Medium
# Pattern: Binary Search — treat 2D matrix as flattened 1D array using row = mid // cols, col = mid % cols — O(log(m*n))

class Solution:
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        while l <= r:
            mid = (l + r) // 2
            row = mid // cols
            col = mid % cols
            val = matrix[row][col]
            if target > val:
                l = mid + 1
            elif target < val:
                r = mid - 1
            else:
                return True
        return False