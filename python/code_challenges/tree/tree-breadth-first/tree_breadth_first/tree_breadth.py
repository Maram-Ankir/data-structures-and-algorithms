

class Node:
  def __init__(self,value):
    self.value= value
    self.next= None

class Queue():
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue (self,value):
        node=Node(value)
        if self.front==None:
            self.front=node
            self.rear=node
            return self.rear.value
        else:
            self.rear.next=node
            self.rear=node
            return self.rear.value

    def dequeue(self):
        try:
            if self.front == None:
              raise Exception
            temp=self.front
            self.front=self.front.next
            return temp.value
        except Exception:
            return 'error'

    def isEmpty(self):
        return self.front==None

    def peek (self):
        try:
            if self.front == None:
                raise Exception
            return self.front.value

        except Exception:
            return 'Empty Queue'

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
