#Creating a class for the Node
class Node:
    def __init__(self, data):
        #Creating a linked list none with three attributes
        #data - the actual data that is stored in the node
        #next - the link to the NEXT node
        #prev - the link to the PREVIOUS node
        self.data = data
        self.prev = None
        self.next = None

#Create a NEW METHOD of node called link()

    def link(self, otherNode):
        #link() should take in ANOTHER node and link THAT
        #link() - should take in the second node and link the
        self.next = otherNode  #forward link
        otherNode.prev = self  #baackwards link

#Create a __str()__ method to retuen adata associated with the node

    def __str__(self):
        return self.data.__str__()


#Creating a class for the linked list
class linkedList:
    def __init__(self):
        #Creating 2 attribtes
        #first - first node on the list
        #last - last node on the list
        self.first = None
        self.last = None

    #Creating a function to add the values onto
    def add(self, item):
        #reate a node for this item
        node = Node(item)
        if self.first is None:
            self.first = node
        else:
            #link the new node to the current last node
            self.last.link(node)

        #updating sef.last to the new node
        self.last = node

    #Creating a function that returns the item with the given index (position)
    #The method will eithe return a Valid node if the index is within the linked list or None if the index is beyond the end of the linked list
    def get(self, index):
        #Represents our current position within the linked list
        counter = 0
        currentNode = self.first
        while currentNode is not None and counter < index:
            #increaes the ocunter by 1
            counter = counter + 1
            #Move node on by 1
            currentNode = currentNode.next
        #Either valid node or None
        return currentNode


#Main program

#Creating a linked list
list = linkedList()
list.add("apple")
list.add("cherry")
list.add("pomergranate")
list.add("grape")

#Testing if the list wil print correctly
#Should be apple
print(list.get(0))
#shoud be grape
print(list.get(3))
#should be None
print(list.get(4))

#Testing to see if it creates
n1 = Node("Fred")
n2 = Node("Tom")

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
