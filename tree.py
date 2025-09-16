class treenode:
  def _init_(self,val):
    self.data = data
    self.children = []
class Tree:
  def _init_(self):
    self.root = None
    
  def odd(self,data,parentdata=None):
    node = treenode(data)
    if not self.root:
      self.root = node
      return
    parentnode = self.findnode(parentnode,self.root) 
    
    [if not parentnode:
      print("parentnode not found")
      return
    parentnode = self.findnode(parentnode,self.root)
    if not parentnode:
      print("Parent not found")
      return
  parentnode.children.append(node)
  
def findnode(self,data,node):
  if node.data == data:
    return node
  for child in node.children:
    nodefound = self.findnode(data,child)
    if nodefound:
      return nodefound
  return None

