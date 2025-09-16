class Node:
  def __init__(self,val):
    self.data = val
    self.next=None
class Queue:
  def __init__ (self):
    self.front=None
    self.rear=None
  def enqueue(self,val):
    newnode=Node(val)
    if self.rear is None:
      self.front=self.rear=newnode
    self.rear.next=newnode
    self.rear=newnode
  def dequeue(self):
    if self.front is None:
      print("Queue is Empty")
    temp=self.front.data
    self.front=self.front.next
    return temp
  def display(self):
    temp=self.front
    while temp:
      print(temp.data,end="-->")
      temp=temp.next
    print("Null")
n=int(input())
a=Queue()
for i in range(n):
  a.enqueue(int(input()))
  
a.display()
print("Deleted term",a.dequeue())

a.enqueue(4)
a.display()
