# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Difficulty: Easy
# Pattern: Floyd's Cycle Detection (slow/fast pointers) — if there's a cycle,
# fast eventually catches up to slow — O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False