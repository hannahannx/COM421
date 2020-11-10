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
    #calculating the hashCode for the value inputed
    hashCode = self.getHashCode(key)
    #Using this value and storing the value inside the list
    bucketIndex = hashCode % 127
    #if there is nothing allocated inside the position then that position should become an empty list
    if self.bucketArray[bucketIndex] is None:
      self.bucketArray[bucketIndex] = []
        #adding the values (key and the value) as a tuple onto the list in that specific position
      self.bucketArray[bucketIndex].append((key,value))
    print(self.bucketArray)

  def get(self,key):
    #Searchig for the item in the HashTable
    hashCode = self.getHashCode(key)
    bucketIndex = hashCode % 127
    #Checking to see if there is something inside that bucket
    if self.bucketArray[bucketIndex] is not None:
      #loop through all of the postions in the value of the postions
      for pairs in self.bucketArray[bucketIndex]:
        if pairs[0] == key:# pairs is a tuple containing the value
          return pairs[1]
      #Shows that nothing has been found
      return None 

  #Calculating the ASCII code for the key
  def getHashCode(self,key):
    hashCode = 0
    #Looping through each character in the key and adding the ord value(ASCII) to the hashCode 
    for value in key:
      convert = ord(value)
      hashCode = hashCode + convert
    return hashCode

  #Creating a function to run the HashTable
  def run():
    hashfunction = HashTable()
    key = input("What value would you like to be used?")
    description = input("Please describe {} ".format(key))
    print("Displaying hashtable.........")
    print()
    hashfunction.put(key,description)
    print(hashfunction.get(key))
    

#Main code
#Testing for one value in the hashtable
HashTable.run()