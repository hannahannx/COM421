#SEPERATE CHAINING MEETHOD 
print("SEPERATE CHAINING METHOD ")
print()
#Creating the list of keys 
i = [36,88,54,28,49,21,63,7,19,2,11,41,34]
#going through all of the values and calculating the has value
for position in range(0,len(i),1):
  if (i[position] == i[position]):
    print ("KEY", i[position] ,"IS IN BUCKET ", (2*i[position]) % 17)
    print ("", end = "")
  else:
    print ((2*i[position]) % 17)
