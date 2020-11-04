#Creating a class for the Queue
class Queue:
  #default capicity would be 5
  def __init__(self,capacity = 5):
    #Initalising the Queue to make sure it has 5 spaces and the maximum capacity would be 5
    self.capacity = 5
    #Where None represents that ther is nothing inside this position
    self.internalArray = [None] * self.capacity
    self.front = 0
    #This would be the next avaible space in the queue
    #This is because items in a queue are always added onto the back of the queue
    self.back = 0
  
  #Adds the next item on the array at the back of the queue
  def add (self,item):
    #When the queue is empty, back should be equal to zero as there is nothing in the queue
    self.internalArray[self.back] = item
    #Before you add the item you would need tto create space for it, so add 1
    self.back = self.back + 1
    #implementing the circular aspect of the queue
    if self.back > len(self.internalArray):
      self.back = 0

  #Removes the first item in the array at the front of the queue and returns it
  def remove (self,item):
    currentFrontItem = self.internalArray[self.front] #Returning the front item
    #The front of there queue is the next item's back
    self.front =  self.front + 1
    #implementing the circular aspect of the queue
    if self.front > len(self.internalArray):
      self.front = 0
    #Returning the front item
    return currentFrontItem
    
    self.front = self.internalArray[len()]

  def __str__(self):
      return self.internalArray.__str__()

#Main program
queue = Queue(6)

#Checking if it will add items onto the array
print("Adding Item")
queue.add(2)
print(queue)
print("Adding Item")
queue.add(4)
print(queue)
print("Adding Item")
queue.add(9)
print(queue)
print("Adding Item")
queue.add(102)
print(queue)
print("Adding Item")
queue.add(28)
print(queue)
#Checking if it will remove items onto the array
print("Removing Item")
queue.remove(28)
print(queue)