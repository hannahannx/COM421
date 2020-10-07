class Stack:
    def __init__(self):
        self.internalArray = []

    def push(self, item):
        # This is code to add an item to the stack will go here
        self.internalArray.append(item)

    def pop(self):
        # Code to remove an item from the top of the stack will go here
        self.internalArray.remove

    def __str__(self):
        return self.internalArray.__str__()

#Initalising the stack
stack1 = Stack()

#printing the empty stack
print(stack1)

#Adding pushing the numbers onto the stack
stack1.push(1)
print(stack1)
stack1.push(4)
print(stack1)
stack1.push(9)
print(stack1)

#Printing the stack
print(stack1)

#Reoving poppin the numbers off the stack
stack1.pop()
print(stack1)