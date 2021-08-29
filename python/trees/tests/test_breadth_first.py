from trees import __version__
from trees import breadth_first,Queue
from trees import Binary_Tree, Node




def test_version():
    assert __version__ == '0.1.0'


def test_breadth_first():
    b_tree=Binary_Tree()
    b_tree.root=Node(2)
    b_tree.root.left=Node(7)
    b_tree.root.left.left=Node(2)
    b_tree.root.left.right=Node(6)
    b_tree.root.left.right.left=Node(5)
    b_tree.root.left.right.right=Node(11)
    b_tree.root.right=Node(5)
    b_tree.root.right.right=Node(9)
    b_tree.root.right.right.left=Node(4)
    expected=[2,7,5,2,6,9,5,11,4]
    actual=breadth_first(b_tree)
    assert expected==actual
