#!/usr/bin/python

#!Creating Lists

ages = [2, 56, 89, 21, 1, 72]
pets = ["Cat", "Dog", "Lizard", "Monkey", "Spider"]

print(ages)
print(pets)

#!Printing out in indices
print(pets[3])
print(ages[2])

#!printing out from the back of the list
print(ages[-3])
print(pets[-2]) #!take note that lists indexing from left-right starts at zero(0) and from right-left start from one(-1)

#!special select
print(pets[2:]) #!here python will grab everything at index position 2 and everything after it
print(ages[1:5]) #!take note here that the list position "5" will not be printed this is because it takes the differential range like (5-1=4) so only 4 elements within the range will be concidered

#!Modify
pets[2] = "Snail"
print(pets[2]) #!here lizard is going to be subsituted by Snail

#!extend the list
pets.extend(ages)
print(ages)
pets.append("Frog") #!will always append a function at the end of the list
print(pets)
ages.insert(2, 10002) #!here 10002 is going to be added at index position "2" and all other elements pusshed one index position
print(ages)

#!remove a value
people = ["sundar", "craig", "gates", "ellen","samantha", "janet"]
people.remove("gates")
people.pop() #!here "pop" removes the last element
print(people)
print(people.index("samantha")) #!here it'll tell me the index of samantha

#!Count values with in the list
electronics = ["microwave", "television", "cable", "satelite", "fridge", "cable"]
print(electronics.count("cable"))
electronics.sort() #!it'll sort in assending order
print(electronics)
electronics.reverse() #!it'll reverse the list
print(electronics)

#!Copy a list
electronics2 = electronics.copy()
print(electronics2)

#!Go Ahead and test it out!!!!
