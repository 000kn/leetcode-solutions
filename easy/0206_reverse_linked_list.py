# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy
# Pattern: Three-pointer technique (prev, curr, next) — save next before
# reversing the link, then advance — O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev