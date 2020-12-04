#importing modules
import math

#Creating the Hoare Partition function
def hoarePartition(listToSort,start,end):
  #Creating the pointers 
  leftPoint = start #i
  rightPoint = end #j
  midpoint = math.floor((start + end)/2 )
  pivot = listToSort[midpoint]
  
  #This will loop forever
  while True:
    #moving the starting position forward
    while listToSort[leftPoint] < pivot:
      leftPoint = leftPoint + 1 
    #moving the ending position backwards
    while listToSort[rightPoint] > pivot:
      rightPoint = rightPoint - 1
    
    if listToSort[leftPoint] < listToSort[rightPoint]:
      #swapping the values
      temp = listToSort[leftPoint]
      listToSort[leftPoint] = listToSort[rightPoint]
      listToSort[rightPoint] = temp
    else:
      return listToSort[rightPoint]

def quickSort(data,start,end):
  if end < start:
    return
  else:
    pivot = hoarePartition(data,start,end)
    quickSort(data,start,end)

unsorted = [22,56,1,59,38,7,15,17]
quickSort(unsorted,0,7)
