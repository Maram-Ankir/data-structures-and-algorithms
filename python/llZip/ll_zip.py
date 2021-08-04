
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




    def zipLists(list1, list2):
        temp='head -> '
        first_ll=list1.head
        second_ll=list2.head
        values=[]
        while first_ll:
            values+=[first_ll.value]
            first_ll = first_ll.next
            if second_ll:
                values+=[second_ll.value]
                second_ll = second_ll.next

        if first_ll==None and second_ll != None:
            while second_ll:
                values+=[second_ll.value]
                second_ll = second_ll.next

        for  i in range(len(values)):
            temp+='{'+f'{values[i]}'+'} '+'-> '
        temp+='NULL'
        return temp






if __name__=='__main__':

    l1=LinkedList()
    l1.append(1)
    l1.append(3)
    l1.append(2)
    l2=LinkedList()
    l2.append(5)
    l2.append(9)
    # l2.append(4)
    print(l1)
    print(l2)
    x=LinkedList.zipLists(l1,l2)
    print(x)
    # print(zip(l1,l2))

