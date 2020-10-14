#Creating a class for the Node
class node:
  def __init__(self, data):
    #Creating a linked list none with three attributes
    #data - the actual data that is stored in the node
    #next - the link to the NEXT node
    #prev - the link to the PREVIOUS node
    self.data = data
    self.prev = None
    self.next = None

#Create a NEW METHOD of node called link()
  def link(self,otherNode):
    #link() should take in ANOTHER node and link THAT 
    #link() - should take in the second node and link the
    self.next = otherNode #forward link
    otherNode.prev = self #baackwards link

#Create a __str()__ method to retuen adata associated with the node
  def __str__(self):
    return self.data.__str__()

#Creating a class for the linked list
class linkedList:
  def __init__(self):
    #Creating 2 attribtes
    #first - firt node on the list
    #last - last node on the list
    self.first = None
    self.last = None
  
  #Creating a function to add the values onto 
  def add():

  
  def get(self,index):


  def 

  



#Main program
#Testing to see if it creates 
n1 = node("Fred")
n2 = node("Tom")

#Printing out the seperate nodes
print("Printing out the nodes.")
print(n1)
print(n2)

#linking the nodes together
n1.link(n2)
#Printing the node
print(n1.prev)
print(n1.next)
print(n2.prev)
print(n2.next)


