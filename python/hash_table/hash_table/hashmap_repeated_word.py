from linked_list import LinkedList

class Hashmap:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def hash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
        index =( sum * 7) % self.size
        return index

    def add(self, key, value):
        idx = self.hash(key)
        if not self._buckets[idx]:
            self._buckets[idx] = LinkedList()
        self._buckets[idx].add([key, value])

    def find(self,key):
        idx=self.hash(key)
        if self._buckets[idx]==None:
            return 'Key not found'
        else:
            current = self._buckets[idx].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next
            raise KeyError("Key not found", key)


    def contains(self,key):
       idx=self.hash(key)
       if self._buckets[idx]==None:
           return False
       else:
            current = self._buckets[idx].head
            while current:
                if current.value[0] == key:
                    return True
                else:
                 return False

    def repeated_word(self,str):
        str_list=str.split()
        hash_map=Hashmap()
        for i in str_list:
            if hash_map.contains(i):
                return f'{i}'
            else:
                hash_map.add(i,i)
        return 'No duplicates'



if __name__ == "__main__":
  hash=Hashmap()

  hash.add('1','maram')
  hash.add('2', 'ali')
  hash.add('3', 'ankir')
  print(hash.repeated_word("Once upon a time "))
  print(hash.repeated_word("Once upon a time a"))

