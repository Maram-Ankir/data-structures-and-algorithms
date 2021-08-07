# from challenges import __version__

from ll_zip.ll_zip import zipLists

from challenges.linked_list import LinkedList


def test_version():
    assert __version__ == '0.1.0'


def test_ll_zip_l1_less_than_l2():
    lnk_lst1=LinkedList()
    lnk_lst1.append(8)
    lnk_lst1.append(3)

    lnk_lst2=LinkedList()
    lnk_lst2.append(4)
    lnk_lst2.append(7)
    lnk_lst2.append(5)
    lnk_lst2.append(6)

    actual= zipLists(lnk_lst1,lnk_lst2)
    expected='head -> {8} -> {4} -> {3} -> {7} -> {5} -> {6} -> NULL'
    assert expected==actual

def test_ll_zip_l1_greater_than_l2():
    lnk_lst1=LinkedList()
    lnk_lst1.append(8)
    lnk_lst1.append(3)
    lnk_lst1.append(5)
    lnk_lst1.append(6)

    lnk_lst2=LinkedList()
    lnk_lst2.append(4)
    lnk_lst2.append(7)

    actual=zipLists(lnk_lst1,lnk_lst2)
    expected='head -> {8} -> {4} -> {3} -> {7} -> {5} -> {6} -> NULL'
    assert expected==actual

def test_ll_zip_l1_equal_l2():
    lnk_lst1=LinkedList()
    lnk_lst1.append(8)
    lnk_lst1.append(3)

    lnk_lst2=LinkedList()
    lnk_lst2.append(4)
    lnk_lst2.append(7)

    actual=zipLists(lnk_lst1,lnk_lst2)
    expected='head -> {8} -> {4} -> {3} -> {7} -> NULL'
    assert expected==actual

def test_ll_zip_l1_empty():
    lnk_lst1=LinkedList()

    lnk_lst2=LinkedList()
    lnk_lst2.append(4)
    lnk_lst2.append(7)
    actual=zipLists(lnk_lst1,lnk_lst2)
    expected='head -> {4} -> {7} -> NULL'
    assert expected==actual

def test_ll_zip_l2_empty():
    lnk_lst1=LinkedList()
    lnk_lst1.append(8)
    lnk_lst1.append(3)

    lnk_lst2=LinkedList()

    actual=zipLists(lnk_lst1,lnk_lst2)
    expected='head -> {8} -> {3} -> NULL'
    assert expected==actual
