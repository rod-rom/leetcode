import pytest
from linked_list.merge_two_sorted_lists import mergeTwoLists, ListNode  # Adjust the import path

# Helper function to convert a list to a ListNode
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a ListNode to a list
def linkedlist_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [0], [0]),
    ([], [], [])
])
def test_merge_two_lists(list1, list2, expected):
    list1_ll = list_to_linkedlist(list1)
    list2_ll = list_to_linkedlist(list2)
    result_ll = mergeTwoLists(list1_ll, list2_ll)
    assert linkedlist_to_list(result_ll) == expected
