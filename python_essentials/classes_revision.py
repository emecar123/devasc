
#All funcions in classes begin with self)
class Robot:
    def __init__(self, name, color, weight):     #constructor (with attribute var.)
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):                      #Method
        print("My name is " + self.name)
        #print("My weight is " + str(self.weight))

# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30
#
# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40

r1 = Robot("Tom", "red", 30)                     #object1
r2 = Robot("Jerry", "blue", 40)                  #object2

r1.introduce_self()
r2.introduce_self()
