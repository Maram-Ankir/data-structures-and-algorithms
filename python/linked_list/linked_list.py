# class LinkedList:
#     """
#     Put docstring here
#     """

#     def __init__(self):
#         # initialization here
#         pass

#     def some_method(self):
#         # method body here
#         pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    inestance=[]

    def __init__(self):
        self.head = None

    def insert(self, value):

        node = Node(value)
        if self.head == None:
            self.head = node
            return self.head.value
        else:
            current = self.head
            self.head = node
            self.head.next = current
            return self.head.value


    def __str__(self):

        if self.head == None:
            return 'NULL'
        else :
            values=''
            temporary_value=self.head
            while temporary_value:
                values+=f'{temporary_value.value}'  + '-> '
                temporary_value=temporary_value.next
            values=values +'NULL'
            return f'{values}'

    def append(self,value):
        current=self.head
        if self.head ==None:
            self.head=Node(value)
            return self.head.value
        else:
            while current.next:
                current=current.next
            current.next=Node(value)
            return current.next

def insert(self, old_data, new_data):

    if self.head is None:
        return

    if self.head.data == old_data:
        self.head.next = Node(new_data, self.head.next)
        return

    temp = self.head

    while temp:
        if temp.data == old_data:
            temp.next = Node(new_data, temp.next)
            break

    temp = temp.next


ll1=LinkedList()
ll1.append(5)
ll1.append(6)
# ll1.insert(6,8)

print(ll1)

