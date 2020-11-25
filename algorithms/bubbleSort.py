#Creating a list in to implemet the bubble sort on
listToSort = ["20","13","17","1"]
print(listToSort)
#going through the list for amount of times in which is in the list
for iteration in range(len(listToSort)-1):
  #swapping the numbers if the alue on the left is larger than the on the right
  for swap in range(len(listToSort)-1):
    #Checking if the current value is less than the  next one
    if listToSort[swap] > listToSort[swap+1]:
      #Showng that they are swapping the values
      print("Swapping")
      #creating a tempory value for the item
      temp = listToSort[swap]
      listToSort[swap] = listToSort[swap+1]
      listToSort[swap+1] = temp
      print(listToSort)
    elif listToSort[swap] < listToSort[swap+1]:
       #Showng that they are not swapping the values
      print("No swap")
  print ("{} Iteration done!!\n".format(iteration+1))
print(listToSort)