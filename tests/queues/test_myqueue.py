import pytest
from queues.implement_queue_using_stacks import MyQueue

def test_queue_push():
    queue = MyQueue()
    queue.push(1)
    assert queue.peek() == 1
    queue.push(2)
    assert queue.peek() == 1  # The first element should still be 1

def test_queue_pop():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1  # Pop should return the first element
    assert queue.pop() == 2  # Now the second element

def test_queue_peek():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1  # Peek should return the first element
    queue.pop()
    assert queue.peek() == 2  # Now peek should return the second element

def test_queue_empty():
    queue = MyQueue()
    assert queue.empty()  # Initially the queue should be empty
    queue.push(1)
    assert not queue.empty()  # Now the queue should not be empty
    queue.pop()
    assert queue.empty()  # The queue should be empty again

# Test for popping from an empty queue
def test_pop_empty_queue():
    queue = MyQueue()
    with pytest.raises(IndexError):
        queue.pop()

# Test for peeking into an empty queue
def test_peek_empty_queue():
    queue = MyQueue()
    with pytest.raises(IndexError):
        queue.peek()
