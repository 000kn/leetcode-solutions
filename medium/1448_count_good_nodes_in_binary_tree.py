# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Difficulty: Medium
# Pattern: DFS with path-max parameter passed down through recursion

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar):
            if not node:
                return 0

            good = 0
            if node.val >= maxSoFar:
                good += 1
                maxSoFar = node.val

            good += dfs(node.left, maxSoFar)
            good += dfs(node.right, maxSoFar)

            return good

        return dfs(root, root.val)