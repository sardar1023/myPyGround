#This is the basic encryption and decryption code

#Encryption
#alphebet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#Key
#key = 3
#newMessage variable
newMessage = ''
newMessage1 = ''
#Enter a character from the console
message = input('Plz Enter a message: ')
key = int(input('Plz Enter your key: '))
#Find the position of the character in the alphabet
for character in message:
  if character in alphabet:
    position = alphabet.find(character)
#Set the new position to the character
    newPosition = (position + key) % 26
#Pull the new character to corresponding new position
    newCharacter = alphabet[newPosition]
   # print("New character is : " , newCharacter)
    newMessage+=newCharacter
  else:
     newMessage+=character
print("Your encripted message is ", newMessage)


#Decryption
for character in newMessage:
  if character in alphabet:
    position = alphabet.find(character)
#Set the new position to the character
    newPosition = (position - key) % 26
#Pull the new character to corresponding new position
    newCharacter = alphabet[newPosition]
   # print("New character is : " , newCharacter)
    newMessage1+=newCharacter
  else:
     newMessage1+=character
print("Your decripted message is ", newMessage1)