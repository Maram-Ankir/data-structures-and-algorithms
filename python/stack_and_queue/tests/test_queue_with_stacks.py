from stack_and_queue.queue_with_stacks import PseudoQueue
# import pytest


def test_enqueue_to_psudeo():
    p_queue=PseudoQueue()
    p_queue.enqueue(5)
    expected=5
    actual= p_queue.rear.top.value
    assert expected==actual


def test_enqueue_None_value():
    p_queue=PseudoQueue()
    expected=False
    actual=p_queue.enqueue(None)
    assert expected==actual

def test_dequeue_from_psudeo():
    p_queue=PseudoQueue()
    p_queue.enqueue(7)
    p_queue.enqueue(4)
    p_queue.dequeue()
    expected=7
    actual=p_queue.dequeue()
    assert expected==actual

