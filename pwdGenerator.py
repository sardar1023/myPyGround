import random
#define a character sequence
char = 'abcdefghijklmnopqrstuvwxyz1234567890'
#Choose the password length
length = int(input('What is your Pwd Lenght? '))
#number of the password
number = int(input('Choose the number of the password '))
#password should be create by random numbers from the char
pwd = ''
password=''
for p in range(number):
    for c in range(length):
      password+= random.choice(char)
    print(password)



