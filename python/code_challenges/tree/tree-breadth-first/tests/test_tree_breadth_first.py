from tree_breadth_first import __version__


def test_version():
    assert __version__ == '0.1.0'



from stack_and_queue import Queue
from trees import Binary_Tree,Node


def breadth_first(tree):

    if not tree:
        return "Tree is Empty"

    values=[]
    breadth=Queue()

    if tree :
        breadth.enqueue(tree.root)


    while not breadth.isEmpty():

        tree_node=breadth.dequeue()
        values+=[tree_node.value]

        if tree_node.left:
            breadth.enqueue(tree_node.left)

        if tree_node.right:
            breadth.enqueue(tree_node.right)

    return values


# b_tree=Binary_Tree()
# b_tree.root=Node(2)
# b_tree.root.left=Node(7)
# b_tree.root.left.left=Node(2)
# b_tree.root.left.right=Node(6)
# b_tree.root.left.right.left=Node(5)
# b_tree.root.left.right.right=Node(11)
# b_tree.root.right=Node(5)
# b_tree.root.right.right=Node(9)
# b_tree.root.right.right.left=Node(4)

# print(b_tree)
