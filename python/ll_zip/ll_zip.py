from linked_list import LinkedList

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





# l1=LinkedList()
# l1.append(1)
# l1.append(3)
# l1.append(2)
# l2=LinkedList()
# l2.append(5)
# l2.append(9)
# l2.append(4)
# print(l1)
# print(l2)
# print(zipLists(l1,l2))
# print(zip(l1,l2))
