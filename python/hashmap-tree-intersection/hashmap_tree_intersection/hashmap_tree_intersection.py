
from hash_table.hash_table import Hashtmap
from trees.trees import Binary_Tree, Node

def tree_intersection(tree1,tree2):
    array=[]
    hashtable=Hashtmap()
    tree_arr1=tree1.pre_order()
    print(tree_arr1)
    tree_arr2=tree2.pre_order()
    print( tree_arr2)
    for item in tree_arr1:
        hashtable.add(item,item)
    print(hashtable)
    for i in tree_arr2:
        if hashtable.contains(i):
            array+=[i]
    if array==[]:
        return 'No intersection'

    return array
