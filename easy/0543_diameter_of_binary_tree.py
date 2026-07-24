# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/
# Difficulty: Easy
# Pattern: DFS + global tracking (self.maxD updated as side effect during depth calculation)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.maxD = max(self.maxD, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.maxD