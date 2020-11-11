#Creating a class called tree node 
#individual node in the tree
class TreeNode:
  #Initalising the class
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None
    
    def insert(self,newValue):
      #recursion used
      #if the newValue is greater than the value at the current node then make it the left child
      if newValue < self.value:
        if self.left is None:
          self.left = TreeNode(newValue)
        else: # if its not None
          self.left.insert(newValue)
      #if the newValue is less than the value at the current node then make it the right child
      elif newValue > self.value:
        if self.right is None:
          self.right = TreeNode(newValue)
        else: #Not none 
          self.right.insert(newValue)

#Creating a class called BInary
class BinaryTree:
  #initalising the class
  #root = node at the top of the tree
  def __init__(self, root):
    #In the beginning the node should have nothing inside
    self.root = None
  
  def insert(self,value):
    #When the tree is completely empty the roots should be None
    if self.root is None:
      #creates the node with the value which is inserted 
      self.root =TreeNode(value)
    else:
      #insert the value into the roots by calling the insert method of treeNode
      self.root.insert(value)

  #printing out the tree contents using recursion  
  def printTree(self,startingNode): #also known as rootNode
    #if the node to the left contains a value
    if startingNode.left is not None:
      #prints out the tree on the left node
      self.printTree(startingNode.left)
      #prints out the starting node value 
    print(startingNode.value)
    if startingNode.right is not None:
      #prints out the tree on the right node
      self.printTree(startingNode.right)
      
#Main program
tree = BinaryTree("")
tree.insert(333)
tree.insert(444)
tree.insert(222)
tree.insert(777)
tree.insert(555)
tree.printTree(tree.root)

