class parent:
    def speak(self):
        print("Speaking")

class child(parent):
    def eat(self):
        print("Eating")


child = child()
child.speak()


parent = parent()
parent.speak()