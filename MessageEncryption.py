'''
The Caesar cipher
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
'''


alphabet='abcdefghijklmnopqrstuvwxyz'

key=int(input("key 1/26  ??"))

message=input("enter a message")
newMessage=''
for character in message:
    if character in alphabet:
        position = int(alphabet.find(character))

        newPosition = (position + key) % 26

        newCharacter = alphabet[newPosition]

        newMessage += newCharacter
    else:
        newMessage += character

print(newMessage)