class Node:
  def __init__(self,value):
    self.value= value
    self.next= None

class Stack():
    def __init__(self):
      self.top=None

    def push(self,value):
      node=Node(value)
      node.next =self.top
      self.top = node

    def pop(self):
        try:
            if self.top ==None:
               raise Exception
            temp=self.top
            self.top=self.top.next
            return temp.value

        except Exception:
            return 'Empty Stack'

    def is_empty(self):
     return not self.top


    def peek(self):
        try:
            if self.top ==None:
               raise Exception
            return self.top.value

        except Exception:
            return 'error'




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


q=Queue()
q.enqueue(4)
print(q)

