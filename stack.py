class Node:
  def __init__(self,val):
    self.data = val
    self.next = None
class stack:
    def __init__(self):
        self.top = None
    def push(self,val):
        newnode = Node(val)
        if self.top is None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        p_ele = self.top.data
        self.top = self.top.next
        return p_ele
    def peek(self):
        if self.top is None:
            print("stack is empty")
        return self.top.data
    def display(self):
        temp = self.top
        while temp:
            print(temp.data,end = "-->")
            temp = temp.next
    
  
  
