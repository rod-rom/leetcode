# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative solution
# Time complexity: O(n)
# Space complexity: O(1)
def reverseListIterative(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


# Recursive solution
# Time complexity: O(n)
# Space complexity: O(n)
def reverseListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:return None
    
    new_head = head
    if head.next:
        new_head = reverseListRecursive(head.next)
        head.next.next = head
    head.next = None

    return new_head
    