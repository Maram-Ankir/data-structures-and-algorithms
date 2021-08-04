# from ll_zip import __version__

from ll_zip import LinkedList
from ll_zip import zipLists




# def test_version():
#     assert __version__ == '0.1.0'


def test_zip_l1_less_than_l2():
    list1=LinkedList()
    list1.append(8)
    list1.append(3)

    list2=LinkedList()
    list2.append(4)
    list2.append(7)
    list2.append(5)
    list2.append(6)

    actual= zipLists(list1,list2)
    expected='head -> {8} -> {4} -> {3} -> {7} -> {5} -> {6} -> NULL'
    assert expected==actual

def test_zip_l1_greater_than_l2():
    list1=LinkedList()
    list1.append(8)
    list1.append(3)
    list1.append(5)
    list1.append(6)

    list2=LinkedList()
    list2.append(4)
    list2.append(7)

    actual=zipLists(list1,list2)
    expected='head -> {8} -> {4} -> {3} -> {7} -> {5} -> {6} -> NULL'
    assert expected==actual

def test_zip_l1_equal_l2():
    list1=LinkedList()
    list1.append(8)
    list1.append(3)

    list2=LinkedList()
    list2.append(4)
    list2.append(7)

    actual=zipLists(list1,list2)
    expected='head -> {8} -> {4} -> {3} -> {7} -> NULL'
    assert expected==actual

def test_ll_zip_l1_empty():
    list1=LinkedList()

    list2=LinkedList()
    list2.append(4)
    list2.append(7)
    actual=zipLists(list1,list2)
    expected='head -> {4} -> {7} -> NULL'
    assert expected==actual

def test_ll_zip_l2_empty():
    list1=LinkedList()
    list1.append(8)
    list1.append(3)

    list2=LinkedList()

    actual=zipLists(list1,list2)
    expected='head -> {8} -> {3} -> NULL'
    assert expected==actual
