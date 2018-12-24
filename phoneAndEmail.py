# This file finds phone numbers and email address on the clipboard. 
# if you don't have pyperclip, you can install the model under python directory
# in the command line prompt, cd {python directory}
# type this command: pip3 install pyperclip
# copy past a block of the text(your text should include phone number and email)
# Run the python program. Your program will filter the phone number and email 4 U
# Resource -- Automate boring stuff with python.
import pyperclip, re
#Create phone regex
phoneRegex =  re.compile(r'''(
   (\d{3}|\(\d{3}\))?               # area code
   (\s|-|\.)?                       # separator
   (\d{3})                          # first 3 digits
   (\s|-|\.)                        # separator
   (\d{4})                          # last 4 digit
   (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extention
   )''',re.VERBOSE)

#Creata email regex.
emialRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      #username
    @                      #@ symbol
    [a-zA-Z0-9.-]+         #domain name
    (\.[a-zA-Z{2,4}])      #dot-something
    )''',re.VERBOSE)

#Find matches in clipboard text.
text =  str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] !='':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)
for groups in emialRegex.findall(text):
    matches.append(groups[0])

#Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


