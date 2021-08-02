
class Node:

  def __init__(self, value=""):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)

class LinkedList():
  def __init__(self):
    self.head = None

  def insert(self, value):
    node = Node(value)
    if self.head:
      node.next = self.head
    self.head = node

  def includes(self,vlaue):
     current=self.head
     while current :
         print(current.value)
         if vlaue ==current.value:
            return True
         current=current.next

     return False

  def __str__(self):
    string = ""
    current = self.head

    while current:
      string += f"{str(current.value)} -> "
      current = current.next
    string += "None"
    return string

  def __repr__(self):
    return "LinkedList()"

if __name__ == "__main__":
  test = LinkedList()
  test.insert(10)
  test.insert(9)
  test.insert(8)
  test.insert(7)
  test.insert(6)


  print(test.includes(5))
  print('**********')
  print(test.includes(7))
