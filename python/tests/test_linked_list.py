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
