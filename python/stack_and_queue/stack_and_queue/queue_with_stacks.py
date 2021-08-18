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

class PseudoQueue:
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()

    def enqueue(self, value):
        self.rear.push(value)
        return self.rear.top.value


    def dequeue(self):

            while self.front:
                temp= self.front.pop()
                self.rear.push(temp)
            val=self.rear.pop()
            while self.rear:
                res=self.rear.pop()
                self.front.push(res)
            return val





# if __name__ == "__main__":
#     stack = Stack()
#     stack.push(7)
#     stack.push(6)
#     q = PseudoQueue()
#     q.stack = stack
#     q.enqueue(4)
#     q.enqueue(2)
#     print(q)
#     # print(stack)
#     q.dequeue()
#     q.dequeue()
#     q.dequeue()
#     print(q)


