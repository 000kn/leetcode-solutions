# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Medium
# Pattern: Two pointers with a gap of n — advance fast n steps first, then
# move both together; when fast reaches the end, slow is right before
# the node to remove. Dummy node handles the case where head itself is removed — O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next