name = "patil"
print("Before : ",name)

def change():
    global name
    name = "Akshay"
    # print(name)



change()
print("After : ",name)