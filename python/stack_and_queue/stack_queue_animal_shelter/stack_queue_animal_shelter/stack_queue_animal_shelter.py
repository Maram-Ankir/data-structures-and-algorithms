# from stack_and_queue.stack_and_queue import Queue


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



class AnimalShelter:
    def __init__(self):
        self.cat=Queue()
        self.dog=Queue()
        self.count=0

    def enqueue(self,animal,pref):
        pref=pref.lower()
        if pref =='cat':
            self.count+=1
            return self.cat.enqueue(animal)

        elif pref=='dog':
            self.count+=1
            return self.dog.enqueue(animal)

        else:
            return None


    def dequeue (self,pref):
        pref=pref.lower()
        if self.is_empty()==False:
         if pref == 'dog':
            return self.dog.dequeue()
         if pref =='cat':
               return self.cat.dequeue()
         else:
            return None
        else:
            print('Empty Queue')

    def is_empty(self):
        if self.count > 0:
            return False
        else:
            return True

# if __name__=="__main__":

#     q=AnimalShelter()
    # print(q.enqueue('lucy','dog'))
    # print(q.enqueue('jac','cat'))
    # print(q)
    # print(q.dequeue('dog'))
    # print(q.is_empty())


