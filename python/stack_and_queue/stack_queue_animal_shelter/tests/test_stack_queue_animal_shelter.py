from stack_queue_animal_shelter import __version__
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter

# def test_version():
#     assert __version__ == '0.1.0'


def test_expected_outcome_enqueue():
    q=AnimalShelter()
    actual=q.enqueue('lucy','dog')
    expected='lucy'
    assert expected==actual

def test_edge_case_enqueue():
    q=AnimalShelter()
    actual=q.is_empty()
    assert actual== True


def test_expected_failure():
    q=AnimalShelter()
    actual=q.enqueue('lucy','fish')
    expected= None
    assert expected==actual

def test_expected_outcome_dequeue():
    q=AnimalShelter()
    actual=q.enqueue('lucy','dog')
    actual=q.dequeue('dog')
    expected='lucy'
    assert expected==actual

def test_edge_case_dequeue():
    q=AnimalShelter()
    actual=q.dequeue('dog')
    expected=None
    assert actual==expected

def test_expected_failure_dequeue():
    q=AnimalShelter()
    actual=q.enqueue('lucy','dog')
    actual=q.enqueue('nimnim','cat')
    actual=q.dequeue('hourse')
    expected=None
    assert expected==actual

