#importing modules

#Creating the Hoare Partition function
def hoarePartition(listToSort,start,end):
  #Creating the pointers 
  leftPoint = start
  rightPoint = end
  midpoint = math.floor((start + end)/2 )
  pivot = listToSort[midpoint]
  
  #This will loop forever
  while True:
    while listToSort[leftPoint] < pivot:
      leftPoint = leftPoint + 1 
    while listToSort[rightPoint] > pivot
      rightPoint = rightPoint - 1
    
if listToSort[leftPoint] != listToSort[rightPoint]:
  