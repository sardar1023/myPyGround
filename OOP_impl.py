#Python is amazing language. You can also implement OOPs concepts through python 
#Resource: https://www.programiz.com/python-programming/object-oriented-programming

####Creat a class object and method####
class Parrot:

    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return "{} is now sings {}".format(self.name,song)

    def dance(self):
        return "{} is now dancing".format(self.name)


blu = Parrot("Blu",10)
woo = Parrot("Woo",15)

print("Blue is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

print(blu.sing("'Happy'"))
print(blu.dance())

###Inheritance####
#Parent Class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

class Penguin(Bird):

    def __init__(self):
        #call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

####Encapsulation####
"""In python we can denote private attribute
using underscore as prefix i.e single "_" or
"__"."""
class computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice = price

c = computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


###Polymorphism--(Use common interface)###
class Airplane:

    def fly(self):
        print("Airplane can fly")

    def swim(self):
        print("AirPlane cannot swim")

class Boat:

    def fly(self):
        print("Boat cannot fly")

    def swim(self):
        print("Boat can swim")

###Let's define a common interface
def flying_test(bird):
    bird.fly()

plane = Airplane()
boat = Boat()

# passing the object
flying_test(plane)
flying_test(boat)

