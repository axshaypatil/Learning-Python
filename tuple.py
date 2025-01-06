#Why to use tuple
# 1. Tuple are Immutable so, once they created cannot be modify(Ensures Data Integrity)
# 2. It is much faster than  list

cars = ("Thar","Scorpio","xuv 700", "creta")
print(type(cars))

number = (20,"Akshay")
print(type(number))

tpl = ("Akshay","20","Navi Mumbai")

for ele in tpl:
    print(ele)

print(tpl[0])


a = (1,1,2,3,4,5)
b = (6,7,8,9,10)

#Concatination

print(a+b)
print(a*2)

#Membership

print(2 in a)

#lenght

print(len(a))

#Maximum
print(max(a))

#min
print(min(a))

#index
print(a.index(2))

#count
print(a.count(1))

#slicing

print(a[0,len(a):-1])

# Reverse a tuple

print(a[::-1])

