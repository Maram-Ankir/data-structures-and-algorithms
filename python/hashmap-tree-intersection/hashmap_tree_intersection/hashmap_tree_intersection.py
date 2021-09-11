
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

################

class Hashmap:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def hash(self,key):
        if type(key)==int:
            sum_of_assci=key
        else:
            sum_of_assci=sum([ord(char) for char in key])
        temp_value=sum_of_assci*19
        hashed_key= temp_value % self.size
        return hashed_key


    def add(self, key, value):
        idx = self.hash(key)
        if not self._buckets[idx]:
            self._buckets[idx] = LinkedList()
        self._buckets[idx].add([key, value])

    def contains(self,key):
       idx=self.hash(key)
       if self._buckets[idx]==None:
           return False
       else:
            current = self._buckets[idx].head
            while current:
                if current.value[0] == key:
                    return True
                else:
                 return False
##############
class Node:
    def __init__(self,value) :
        self.value=value
        self.left=None
        self.right=None

class Binary_Tree:
    def __init__(self):
        self.root = None
    def pre_order(self):
            self.values=[]
            if self.root == None:
                return "Tree is Empty"
            def tree(node):
               self.values+=[node.value]
               if node.left:
                    tree(node.left)
               if node.right:
                    tree(node.right)
               return self.values
            return tree(self.root)


class Binary_Search_Tree(Binary_Tree):

    def add(self,value):
        if self.root == None:
            self.root = Node(value)
        else:

            current=self.root
            while current:
                if  value < current.value :
                    if current.left == None:
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right == None:
                        current.right = Node(value)
                        break
                    current = current.right
   #################

def tree_intersection(t1,t2):
    array=[]
    hashtable=Hashmap()
    if t1.root== None or t2.root==None:
        return 'empty'
    arr1=t1.pre_order()
    print(arr1)
    arr2=t2.pre_order()
    print(arr2)
    for item in arr1:
        hashtable.add(item,item)
    print(hashtable)
    for i in arr2:
        if hashtable.contains(i):
            array+=[i]
    if array==[]:
        return 'No intersection'
    return array
