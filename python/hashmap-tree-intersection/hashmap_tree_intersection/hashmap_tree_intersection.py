
from hashmap_tree_intersection import Hashtmap ,Binary_Tree, Node


def tree_intersection(bt1,bt2):
    array=[]
    hashtable=Hashtmap()
    if bt1.root== None or bt2.root==None:
        return 'input tree is empty'
    tree_arr1=bt1.pre_order()
    print(tree_arr1)
    tree_arr2=bt2.pre_order()
    print( tree_arr2)
    for item in tree_arr1:
        hashtable.add(item,item)
    print(hashtable)
    for element in tree_arr2:
        if hashtable.contains(element):
            array+=[element]
    if array==[]:
        return 'input Trees have No intersection'
    return array

if __name__=='__main__':
    bt1=Binary_Tree()
    bt1.root=Node(150)
    bt1.root.left=Node(100)
    bt1.root.right=Node(250)
    bt1.root.left.left=Node(75)
    bt1.root.left.right=Node(160)
    bt1.root.right.left=Node(200)
    bt1.root.right.right=Node(350)
    bt1.root.left.right.left=Node(125)
    bt1.root.left.right.right=Node(175)
    bt1.root.right.right.left=Node(300)
    bt1.root.right.right.right=Node(500)

    bt2=Binary_Tree()
    bt2.root=Node(42)
    bt2.root.left=Node(100)
    bt2.root.right=Node(600)
    bt2.root.left.left=Node(15)
    bt2.root.left.right=Node(160)
    bt2.root.right.left=Node(200)
    bt2.root.right.right=Node(350)
    bt2.root.left.right.left=Node(125)
    bt2.root.left.right.right=Node(175)
    bt2.root.right.right.left=Node(4)
    bt2.root.right.right.right=Node(500)

    print(tree_intersection(bt1,bt2))
