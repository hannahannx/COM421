#importing the module 
import math
def binarySearch(listToCompare,numberToSearch):
  #Creating the indexes for the start and the end of the list
  start = 0
  end = len(listToCompare)-1
  
  #Checking to see how big the list is
  while start <= end :
    mid = int((start + end)/2)
    if listToCompare[mid] == numberToSearch:
      print("The value {} is at postion {}".format(numberToSearch,mid))
      break
    else:
      if listToCompare[mid] > numberToSearch:
        end = mid+1
      elif listToCompare[mid] < numberToSearch:
        start = mid-1
      else:
        print("Your number is not in the list")


def run():
  #Asking for user input
  listToCompare = [i*i for i in range(1,101)]
  numberToSearch = int(input("Please enter a number to search for: "))
  binarySearch(listToCompare,numberToSearch)

#Main Program
run()
