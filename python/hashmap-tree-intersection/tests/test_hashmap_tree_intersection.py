import pytest
from hashmap_tree_intersection import __version__
from hashmap_tree_intersection.hashmap_tree_intersection import tree_intersection
from hashmap_tree_intersection.tree import Binary_Tree,Node

def test_version():
    assert __version__ == '0.1.0'

def test_success1(tree_1):
    actual= tree_intersection(tree_1[0],tree_1[1])
    expected=[100,5,250]
    assert actual == expected


def test_success2(tree_2):
    actual= tree_intersection(tree_2[0],tree_2[1])
    expected=[50,27,68]
    assert actual == expected


def test_tree_empty():
    bt1=Binary_Tree()
    bt2=Binary_Tree()
    actual= tree_intersection(bt1,bt2)
    expected='input tree is empty'
    assert actual == expected

def test_tree_no_intersection(tree_3):
    actual= tree_intersection(tree_3[0],tree_3[1])
    expected='input Trees have No intersection'
    assert actual == expected

@pytest.fixture
def tree_1():
    bt1=Binary_Tree()
    bt1.root=Node(100)
    bt1.root.left=Node(85)
    bt1.root.left.left=Node(5)
    bt1.root.right=Node(306)
    bt1.root.left.right=Node(16)
    bt1.root.right.left=Node(250)

    bt2=Binary_Tree()
    bt2.root=Node(100)
    bt2.root.left=Node(50)
    bt2.root.right=Node(200)
    bt2.root.left.left=Node(5)
    bt2.root.left.left.right=Node(13)
    bt2.root.right.right=Node(250)

    return bt1,bt2

@pytest.fixture
def tree_2():
    bt1=Binary_Tree()
    bt1.root=Node(99)
    bt1.root.left=Node(50)
    bt1.root.left.left=Node(27)
    bt1.root.left.left.left=Node(16)
    bt1.root.right=Node(68)


    bt2=Binary_Tree()
    bt2.root=Node(100)
    bt2.root.left=Node(50)
    bt2.root.left.left=Node(27)
    bt2.root.left.left.left=Node(13)
    bt2.root.right=Node(68)

    return bt1,bt2

@pytest.fixture
def tree_3():
    bt1=Binary_Tree()
    bt1.root=Node(48)
    bt1.root.right=Node(50)
    bt1.root.left=Node(27)
    bt1.root.left.left=Node(16)
    bt1.root.right.right=Node(68)

    bt2=Binary_Tree()
    bt2.root=Node(101)
    bt2.root.left=Node(51)
    bt2.root.left.left=Node(28)
    bt2.root.left.left.left=Node(13)
    bt2.root.left.right=Node(69)

    return bt1,bt2
