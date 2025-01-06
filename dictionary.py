student = {"Name" : "Akshay","Age":20,"City":"Navi Mumbai"}
print(student.keys())

# Accessing values
print(student.items())

# Accessing values using keys
print(student.get("Name"))

# Updating values
student.update({"City":"Kolhapur"})
print(student)

# Removing a key-value pair
student.pop("City")
print(student)


#Traverse a Dictionary
student = {"Name" : "Akshay","Age":20,"City":"Navi Mumbai"}
for key in student:
    print(f"Key : {key},  Values : {student[key]}")

print("-------------------------------------------------------")

for key,value in student.items():
    print(f"Key : {key},  Values : {value}")

    