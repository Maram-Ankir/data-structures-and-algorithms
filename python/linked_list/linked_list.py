
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

    def insert_before(self,val,new_val):
            if self.head ==None:
                self.head=Node(val)
            if self.head.value == val:
                self.insert(new_val)
            else:
                try:
                    current=self.head
                    while current.next:
                        if  current.next.value== val:
                            saved_current_val=current.next
                            current.next=Node(new_val)
                            current.next.next=saved_current_val
                            return current.next
                        current=current.next
                except:
                    raise Exception (f'{val} is not in linked list')


    def insert_after(self,val,new_val):
        try:
            current=self.head
            if self.head ==None:
                self.head=Node(val)
                return self.head
            else:
                while current:
                    if  current.value== val:
                        saved_current_val=current.next
                        current.next=Node(new_val)
                        current.next.next=saved_current_val
                        return current.next
                    current=current.next
        except:
            raise Exception ('Error')


# ll1=LinkedList()
# ll1.append(5)
# ll1.append(7)
# ll1.insert_after(5,6)

# print(ll1)

