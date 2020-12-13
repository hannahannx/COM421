def partiton(alist,start,end):
  piviot = alist[start]
  leftmark = start + 1
  rightmark = end
  done = False
  while done == False:
    while (leftmark <= rightmark) and (alist[leftmark] <= piviot):
      leftmark = leftmark + 1
    while (alist[rightmark] >= piviot) and (rightmark>=leftmark):
      rightmark = rightmark - 1
    if rightmark < leftmark:
      done = True
    else:
      temp = alist[leftmark]
      alist[leftmark] = alist[rightmark]
      alist[rightmark] = temp
  
  temp = alist[start]
  alist[start] = alist[rightmark]
  alist[rightmark] = temp
  return rightmark

def quicksort(alist,start,end):
  if start < end :
    split = partiton(alist,start,end)
    quicksort(alist,start,split-1)
    quicksort(alist,split+1,end)
    print("Partitioning")
  return alist
  
alist = ['hannah','amy','chloe','savannah','nevaeh','milly']
sortedList = quicksort(alist,0,len(alist)-1)
print(sortedList)
