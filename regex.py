import re
###function to meet the regular expression condition

def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
###To test the function, we give some input in here
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242')) #This will return True
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))#This will return false

###In here we have a message text
message = 'Call me at 703-479-1874 tomorrow. 222-456-9874 is my office.'
### Loop through whole meassge
for i in range (len(message)):
    ###Every chunk is 12 digit part of the message
    chunk = message[i:i+12]
    ###If it is meet the condition of the function we defined above
    if isPhoneNumber(chunk):
        ###print the phone number value 
        print('Phone numnber found: ' + chunk)
###print Done after everything is finished
print('Done')

###Import re model on the top and define our phone number pattern 
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
###Search the value inside from the text
mo = phoneNumRegex.search('My number is 222-456-7897.')
### print the value
print('Phone number is found ' + mo.group(1))
print('Phone number is found ' + mo.group(2))
print('Phone number is found ' + mo.group(0))

###You can do multiple String match like below
#batRegex = re.compile(r'Bat(man|mobile|copter|bat)') --Multiple option
#batRegex = re.compile(r'Bat(wo)?man')  --Selective option

