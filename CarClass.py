#This example includes Class/Object/Constructor/functions 
#We Create a Car class in here
class Car: 
    #this is our constructor(__int__)
    #Will initiate three parameter value
    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0
   #This is a function to update you car's current speed
    def say_state(self):
        print("I'm going {} mph".format(self.speed))
    #Function of acceleration
    #Every time you call this function, it will increase the speed value by 5 mph
    def accelerate(self):
        self.speed += 5
    #Function of decreasing the speed
    #Every time you call this function, it will decrease the speed value by 5 mph
    def brake(self):
        self.speed -= 5
   #This is the function which records the milage on the Car
    def step(self):
        self.odometer +=self.speed
        self.time += 1
    #This is the function of return the avarage speed
    def avarage_speed(self):
        return self.odometer / self.time
  # This is the statement of declaring Main function  
if __name__ == '__main__':
   #Instantiate an object from the Car class
    my_car = Car()
    #Make sure your car is ready!
    print('I am a car')
    #Declare our While loop in here
    while True:
        #If your choice is not "A,B,O,S", Then program will say I don't know
        action = input("What should I do? [A]ccelerate, [B]rake, "
            "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action)!= 1:
          print("I don't know how to do that ")
          continue
          #option A is acceleration
        if action == 'A':
            #Call accelerate() function from Car class
           my_car.accelerate()
            #option B is brake
        elif action == 'B':
            #Call brake() function from Car class
            my_car.brake()
              #option O is odometer update
        elif action == 'O':
            #Display odometer parameter from Car class
            print("The car has driver {} mile".format(my_car.odometer))
            #option S is avarage speed
        elif action == 'S':
            #Display avarage speed, Call it from Car class
            print("The car's avarage speed was {} mph".format(my_car.avarage_speed))
        #Call step function
        my_car.step()
        #Call say_state function  
        my_car.say_state()
            