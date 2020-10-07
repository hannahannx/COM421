#Creating a stack class with the pop and push methods
class Stack:
    def __init__(self):
        self.internalArray = []

    def push(self, item):
        # This is code to add an item to the stack will go here
        self.internalArray.append(item)

    def pop(self):
       #checking if the list is empty
      if len(self.internalArray) == 0:
        print("Stack is empty - cannot pop")
      else:
        #store the currnt top of stackin the varibale 
        a = self.internalArray[-1]
        # Code to remove an item from the top of the stack will go here
        #We are trying to delete the last member of the array
        # try to delete the last member of the array as the -1 means to remove it
        del self.internalArray[-1]
        # and return it so the outside world can access it
        return a 

    def __str__(self):
        return self.internalArray.__str__()

#Initalising the stack
stack1 = Stack()

#printing the empty stack
print(stack1)

print("pushing")
#Adding (pushing) the numbers onto the stack
stack1.push(1)
print(stack1)
stack1.push(4)
print(stack1)
stack1.push(9)
print(stack1)
#Printing the stack
print(stack1)

print("popping")
stack1.pop()
print(stack1)
stack1.pop()
print(stack1)
stack1.pop()
print(stack1)
stack1.pop()
print(stack1)


