 #SEPERATE CHAINING MEETHOD 
#print("SEPERATE CHAINING METHOD ")
#print()
#Creating the list of keys 
#i = [36,88,54,28,49,21,63,7,19,2,11,41,34]
#going through all of the values and calculating the has value
#for position in range(0,len(i),1):
  #if (i[position] == i[position]):
    #print ("KEY", i[position] ,"IS IN #BUCKET ", (2*i[position]) % 17)
    #print ("", end = "")
  #else:
    #print ((2*i[position]) % 17)

#Creating a class for the hashing function
class HashTable:
  #Initalising the class
  def __init__(self,capacity = 127):
    self.bucketArray = [None] * capacity
  
  #Making a method to put the values inside of the hashtable
  def put(self,key,value):
    hashCode = self.getHashCode(key)
    #Using this value and storing the value inside the list
    bucketIndex = hashCode % 127
    if self.bucketArray[bucketIndex] is None:
      self.bucketArray[bucketIndex] = []
        #adding the values as a tuple onto the list
      self.bucketArray.insert(bucketIndex,[key,value])
    print(self.bucketArray)

  def get(self,key):
    pass

  #Calculating the ASCII code for the key
  def getHashCode(self,key):
    hashCode = 0
    for value in key:
      convert = ord(value)
      hashCode = hashCode + convert
    return hashCode


  def run():
    pass

#Main code
#Testing for one value in the hashtable
hashfunction = HashTable()

hashfunction.put("cat","A type of animal")