#Let's create a very basic calculator in python

#This is our add function
def add(x , y):
    return x + y

#This function subtract two numbers
def subtract(x , y):
    return x - y

#This can help you to divide two number
def divide(x , y):
    return x / y

#The last on is about multipication
def multiply(x , y):
    return x * y

#Thoes are the print lines will give you the choice
print("Select the operation you want!..")
print("1. Add")
print("2. Suntraction")
print("3. Divide")
print("4. Multiply")

#Main part of the code
choice = input("Enter choice(1/2/3/4):")

#Enter 2 target number as num1 and num2
num1 = int(input("Enter the first num: "))
num2 = int(input("Enter the second num: "))

#We make a decision in here via entering number
if choice =='1':
    print(num1,"+",num2,"=",add(num1,num2))
    
elif choice =='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
    
elif choice =='3':
    print(num1,"/",num2,"=",divide(num1,num2))
    
elif choice =='4':
    print(num1,"*",num2,"=",multiply(num1,num2))

else :
    print("Invalid Input")
