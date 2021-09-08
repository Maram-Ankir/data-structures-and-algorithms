
from hash_table.hash_table.hashmap_repeated_word import Hashmap
from hash_table.hash_table.linked_list import LinkedList

def left_join(hasht1,hasht2):
    array =[]
    for i in hasht1._buckets:
        if i != None:
            temp =i.head
            current= temp.value
            while current:
                key = list(current.keys())[0]
                if hasht2.contains(key):
                    array+=[[key,current[key],hasht2.find(key)]]
                else:
                    array+=[[key,current[key],None]]
                if temp.next:
                    temp=temp.next
                    current=temp.value

    return array


#######################
if __name__ == "__main__":
    ht1 = Hashmap()
    ht1.add('fond', 'enamored')
    ht1.add('wrath', 'anger')
    ht1.add('diligent', 'employed')
    ht1.add('outfit', 'grap')
    ht1.add('guide', 'usher')

    ht2 = Hashmap()
    ht2.add('fond', 'averse')
    ht2.add('wrath', 'delight')
    ht2.add('diligent', 'idle')
    ht2.add('guide', 'follow')
    ht2.add('flow', 'jam')

print(left_join(ht1,ht2))
