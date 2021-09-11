from hashmap_tree_intersection import __version__
from hashmap_tree_intersection.hashmap_tree_intersection import tree_intersection
from hashmap_tree_intersection.tree import Binary_Tree,Node

def test_version():
    assert __version__ == '0.1.0'

def test_success():
    t1=Binary_Tree()
    t1.root=Node(100)
    t1.root.left=Node(85)
    t1.root.left.left=Node(5)
    t1.root.right=Node(306)
    t1.root.left.right=Node(16)
    t1.root.right.left=Node(250)
    t2=Binary_Tree()
    t2.root=Node(100)
    t2.root.left=Node(50)
    t2.root.right=Node(200)
    t2.root.left.left=Node(5)
    t2.root.left.left.right=Node(13)
    t2.root.right.right=Node(250)
    actual= tree_intersection(t1,t2)
    assert actual == [100,5,250]


def test_tree_empty():
    t1=Binary_Tree()
    t2=Binary_Tree()
    actual= tree_intersection(t1,t2)
    expected='empty'
    assert actual == expected

def test_tree_no_intersection(tree_3):
    t1=Binary_Tree()
    t1.root=Node(48)
    t1.root.right=Node(50)
    t1.root.left=Node(27)
    t1.root.left.left=Node(16)
    t1.root.right.right=Node(68)
    t2=Binary_Tree()
    t2.root=Node(101)
    t2.root.left=Node(51)
    t2.root.left.left=Node(28)
    t2.root.left.left.left=Node(13)
    t2.root.left.right=Node(69)
    actual= tree_intersection(t1,t2)
    expected='No intersection'
    assert actual == expected
