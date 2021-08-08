from stack_and_queue.stack_and_queue import  Stack


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


