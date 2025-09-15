class Node:
  def __init__(self,val):
    self.data = val
    self.next = None
    #--------------------------------------------------------------------------
class Linkedlist:
  def __init__(self):
    self.head = None
  def insert(self,val):
    newnode = Node(val)
    if self.head is None:
      self.head = newnode
    else:
      temp = self.head
      while temp.next is not None:
        temp = temp.next
      temp.next = newnode
      #--------------------------------------------------------------------------
  def display(self):
    if self.head is None:
      print("Linkedlist is Empty")
    temp = self.head
    while temp is not None:
      print(temp.data,end="-->")
      temp = temp.next
    print("Null")
    #----------------------------------------------------------------------------
  def insert_be(self,val):
    newnode = Node(val)
    if self.head is None:
      self.head = newnode
    temp = self.head
    newnode.next = temp
    self.head = newnode 
    #--------------------------------------------------------------------------------
  def spec(self,val,pos):
    newnode = Node(val)
    if pos == 1:
      self.insert_be(val)
    if pos < 1:
      print("ent valid input")
    temp = self.head
    for i in range(1,pos-1):
      temp = temp.next
    newnode.next = temp.next
    temp.next = newnode
    #-----------------------------------------------------------------------------------
  def del_at_b(self):
    if self.head is None:
      print("none")
    self.head = self.head.next
    #-------------------------------------------------------------------------------------
  def del_at_end(self):
    if self.head is None:
      print("list is empty")
    temp = self.head
    while temp.next.next is not None:
      temp = temp.next
    temp.next=None
    #------------------------------------------------------------------------------------
    def del_at_pos(self,pos):
    if self.head is None:
      print("List is empty")
      return
    if pos == 1: 
      self.head = self.head.next
      return
    temp = self.head
    for i in range(1,pos-1):
      if temp is None or temp.next is None: 
        print("Position out of range")
        return
      temp = temp.next
    if temp.next is None:
      print("Position out of range")
      return
    temp.next = temp.next.next
    #-----------------------------------------------------------------------------------------------------------
list1 = Linkedlist()
n = int(input())
for i in range(n):
  val = int(input())
  list1.insert(val)
  
num = 35
list1.display()

list1.spec(num,3)
list1.display()

list1.spec(num,1)
list1.display()

list1.del_at_b()
list1.display()

list1.del_at_end()
list1.display()

list1.del_at_pos(2)   
list1.display()
