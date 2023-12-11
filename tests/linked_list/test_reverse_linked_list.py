import pytest
from linked_list.reverse_linked_list import ListNode, reverseListIterative, reverseListRecursive

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2], [2, 1]),
    ([1, 2, 3], [3, 2, 1]),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
]

@pytest.mark.parametrize("reverse_function", [reverseListIterative, reverseListRecursive])
@pytest.mark.parametrize("input_list, expected_output", test_cases)
def test_reverse_list_functions(reverse_function, input_list, expected_output):
    input_linked_list = create_linked_list(input_list)
    reversed_linked_list = reverse_function(input_linked_list)
    assert linked_list_to_list(reversed_linked_list) == expected_output
