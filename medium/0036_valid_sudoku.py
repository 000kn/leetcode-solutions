# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# Difficulty: Medium
# Pattern: Hash sets per row/col/box (Arrays & Hashing)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)

        for c in range(9):
            for r in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if val in rows[r] or val in cols[c] or val in boxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)

        return True