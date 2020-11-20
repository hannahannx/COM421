#Creating a list in to implement the selection sort on
print()
listToSort = ["20","13","17","1"]

#Setting the index length for the list
index = range(0,len(listToSort)-1)
#Going through the list for the amount of elements that are in the list
for currentPosition in index:
  #Making the minimum value to compare each of the other value in the 
  minValue = currentPosition
  #looking at the unsorted elements in the list to sort
  for element in range(currentPosition+1, len(listToSort)):
    if listToSort[element] < listToSort[minValue]:
      minValue = element
      print(listToSort)
      print("Moving!!")
      print()
    if minValue != currentPosition:
      listToSort[minValue], listToSort[currentPosition] = listToSort[currentPosition], listToSort[minValue]

print(listToSort)