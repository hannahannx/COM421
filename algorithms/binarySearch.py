#importing the module 
import math
def binarySearch(listToCompare,numberToSearch):
  #Creating the indexes for the start and the end of the list
  start = 0
  end = len(listToCompare)-1
  num = -10
  #Checking to see how big the list is
  while start <= end :
    mid = int((start + end)/2)
    if listToCompare[mid] == numberToSearch:
      print("The value {} is at postion {}".format(numberToSearch,mid))
      num = mid 
      break
    else:
      if listToCompare[mid] > numberToSearch:
        end = mid-1
      else:
        start = mid+1
  return num
  
def run():
  #Asking for user input
  listToCompare = [i*i for i in range(1,101)]
  numberToSearch = int(input("Please enter a number to search for: "))
  value = binarySearch(listToCompare,numberToSearch)
  if value == -10:
    print("Your number is not in the list")

#Main Program
run()
