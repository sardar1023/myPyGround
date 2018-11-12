
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

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 703-479-1874 tomorrow. 222-456-9874 is my office.'

for i in range (len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone numnber found: ' + chunk)
print('Done')