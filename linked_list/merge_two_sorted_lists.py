#https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# recursive solution
# Trick: Use recursion to merge the lists
def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1:
        return list2
    elif not list2:
        return list1
    elif list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2