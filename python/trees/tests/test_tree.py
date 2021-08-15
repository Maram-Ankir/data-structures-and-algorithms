from trees import __version__
from trees.trees import  Binary_Tree, Node, Binary_Search_Tree

# import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_instantiate_an_empty_tree():
    b=Binary_Search_Tree()
    actual=b.root
    expected=None
    assert actual==expected

def  test_instantiate_tree_single_root_node():
    b_tree=Binary_Search_Tree()
    b_tree.add(5)
    b_tree.add(3)
    b_tree.add(8)
    actual=b_tree.root.value
    expected=5
    assert actual==expected


def test_add_left_child_right_child_single_root():
    b_tree=Binary_Search_Tree()
    b_tree.add(5)
    b_tree.add(3)
    b_tree.add(8)
    actual=(b_tree.root.left.value,b_tree.root.right.value)
    expected=(3,8)
    assert actual==expected


def test_collection_from_preorder_traversal():
    b_tree=Binary_Search_Tree()
    b_tree.add(5)
    b_tree.add(3)
    b_tree.add(8)
    actual=b_tree.pre_order()
    expected=[5,3,8]
    assert actual==expected

def test_collection_from_inorder_traversal():
    b_tree=Binary_Search_Tree()
    b_tree.add(5)
    b_tree.add(3)
    b_tree.add(8)
    actual=b_tree.in_order()
    expected=[3,5,8]
    assert actual==expected


def test_collection_from_postorder_traversal():
    b_tree=Binary_Search_Tree()
    b_tree.add(5)
    b_tree.add(3)
    b_tree.add(8)
    actual=b_tree.post_order()
    expected=[3,8,5]
    assert actual==expected
