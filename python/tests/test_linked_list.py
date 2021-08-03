from linked_list.linked_list import LinkedList


# def test_import():
#     assert LinkedList


def test_multiple():
    l=LinkedList()
    l.append(2)
    l.append(8)
    actual=l.__str__()
    expected='2-> 8-> NULL'
    assert actual==expected


def test_one():
    l=LinkedList()
    l.append(2)
    actual=l.__str__()
    expected='2-> NULL'
    assert actual==expected


def test_insert_before_middle_of_linked_list():
    l=LinkedList()
    l.append(8)
    l.append(3)
    l.append('b')
    l.append('4')
    l.insert_before('b',7)
    excepted='{8} -> {3} -> {7} -> {b} -> {4} -> NULL'
    actual=l.__str__()
    assert excepted==actual


def test_insert_before_the_first_node():
    l=LinkedList()
    l.append(5)
    l.append(3)
    l.insert_before(5,'a')
    excepted='{a} -> {5} -> {3} -> NULL'
    actual=l.__str__()
    assert excepted==actual

def test_insert_after_middle_of_linked_list():
    l=LinkedList()
    l.append(8)
    l.append(3)
    l.append('b')
    l.append('4')
    l.insert_after('b',7)
    excepted='{8} -> {3} -> {b} -> {7} -> {4} -> NULL'
    actual=l.__str__()
    assert excepted==actual

def test_insert_after_last_node():
    l=LinkedList()
    l.append(8)
    l.append(3)
    l.insert_after(8,'a')
    excepted='{8} -> {a} -> {3} -> NULL'
    actual=l.__str__()
    assert excepted==actual


def test_k_greater_than_L_list_length():
    l=LinkedList()
    l.append(8)
    l.append(3)
    l.insert_after(8,'a')
    excepted='Error! index out of range'
    actual=l.kthFromEnd(4)
    assert excepted==actual

def  test_k_and_length_of_list_the_same():
    l=LinkedList()
    l.append(8)
    l.append(3)
    l.insert_after(8,'a')
    excepted='Error! index out of range'
    actual=l.kthFromEnd(3)
    assert excepted==actual

def test_k_not_positive_integer():
    l=LinkedList()
    l.append(8)
    l.append(3)
    l.insert_after(8,'a')
    excepted="Error! k can't be negative number"
    actual=l.kthFromEnd(-3)
    assert excepted==actual


def test_linked_list_of_size_1():
    l=LinkedList()
    l.append(8)
    excepted=8
    actual=l.kthFromEnd(0)
    assert excepted==actual

def test_happy_path():
    l=LinkedList()
    l.append(8)
    l.append(3)
    l.insert_after(8,'a')
    excepted='a'
    actual=l.kthFromEnd(1)
    assert excepted==actual
