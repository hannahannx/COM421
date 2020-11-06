# Numpy: Third party libary for manging arrays and performing numerical and mathmatical operations with Python

import numpy 
 #numpy.org - the website for numpy and explainin how it works

#The numPy array is a true array this means that it is a fixed size and we cannot amend it
# It array has an size of 3 so we cannot add or extend it  with the 5th and 4th members 
array1 =numpy.array(["Linux","Windows","Mac OS X"])
print(array1[0]) #prints Linux
print(array1[2])

#These would come back as erorrs
array1[3] = "Android"
array1[3] = "iOS"
#You would be able only to overwrite the elements which are in the lists i.e.
array1[2] = "iOS"
