'''
sets are collections of unique and unordered elements
  #1 . Mutable
  #2 . Unique
  #3 . Unordered  

  why to use set?
  1. uniqueness of elements
  2. Efficient execution of operations like union, intersection, difference

'''

#Creating a List
set1 = {"Akshay","Akshay","Ajay","Vijay","Raj"}
print(set1)

# passing a list into set function
list = [1,2,3,3,4,4,5,6,7]
set2 = set(list)
print(set2)

#Single element in set
set3 =  {"Akshay"}
print(type(set3))
print(set3)

#Empty Set
set4 = {}  #it will create a empty dictionary not a set
set4 = set()  # it will create a empty set
print(type(set4))
print(set4)

#set Fuctions

a = {1,2,3,4,5}
b = {6,7,8,9,10}

#add
a.add(11)
print(a)

#remove

b.remove(7) #if element is not present it will give an error
print(b)

#discard

b.discard(7) #if element is not present it will not give an error
print(b)

#pop
b.pop() #it will remove the random elements
print(b)

#clear
b.clear() #it will remove all the elements


#Mathematical operations

a = {1,2,3}
b = {4,5,6,3}

#union

print("union : ",a | b)

#intersection

print("Intersection : ", a & b)


#symmetric-difference

print("Symmeyric difference", a ^ b)

#difference

print("Difference : " , a - b)


#issubset

print("issubset : ", a.issubset(b))



