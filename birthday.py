#This is the Simple Dictionary object project
#We define the dictionary called birthdays
#We can access and add the new value to the dictionary 
birthdays = {'Sardar': 'Apr 1', 'Yali': 'Dec 12', 'Amina': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name =='':
        break;

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
