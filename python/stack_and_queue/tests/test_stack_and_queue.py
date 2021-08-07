from stack_and_queue import __version__
from stack_and_queue.stack_and_queue import Stack,Queue

# def test_version():
#     assert __version__ == '0.1.0'


def test_push_into_stack():
     stack=Stack()
     stack.push(5)
     excepted=stack.top.value
     assert excepted == 5


def test_push_multiple_values_onto_stack():
    stack=Stack()
    stack.push(4)
    stack.push(8)
    actual=stack.top.value
    expected=8
    assert actual==expected


def test_pop_off_the_stack():
    stack=Stack()
    stack.push(3)
    stack.push(5)
    stack.pop()
    actual=stack.top.value
    expected=3
    assert actual==expected


def test_empty_stack_after_multiple_pops():
    stack=Stack()
    stack.push(4)
    stack.push(8)
    stack.pop()
    stack.pop()
    actual=stack.top
    expected=None
    assert actual==expected

def test_peek_next_item_on_the_stack():
    stack=Stack()
    stack.push(4)
    stack.push(6)
    actual=stack.top.next.value
    expected=4
    assert actual==expected

def test_instantiate_empty_stack():
    stack=Stack()
    actual=stack.top
    expected=None
    assert actual==expected


def test_pop_or_peek_empty_stack():
    stack=Stack()
    actual= stack.pop() or stack.peek()
    expected='Empty Stack'
    assert actual==expected

def test_enqueue_into_queue():
    queue=Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    actual= queue.enqueue(4)
    expected=4
    assert actual==expected


def test_enqueue_multiple_values_to_queue():
    queue=Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    actual= queue.rear.value
    expected=5
    assert actual==expected


def test_dequeue_out_of_queue():
    queue=Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    queue.dequeue()
    actual=queue.front.value
    expected=5
    assert actual==expected


def test_peek_into_queue():
    queue=Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    actual=queue.front.value
    expected=4
    assert actual==expected

def test_empty_queue_after_multiple_dequeues():
    queue=Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    queue.dequeue()
    queue.dequeue()
    actual=queue.front
    expected=None
    assert actual==expected

def test_instantiate_empty_queue():
    queue=Queue()
    actual=queue.front
    expected=None
    assert expected==actual

def test_dequeue_or_peek_empty_queue():
    queue=Queue()
    actual=queue.peek() or queue.dequeue()
    excepted='Empty Queue'
    assert excepted==actual

