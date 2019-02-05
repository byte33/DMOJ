print("Hello and welcome to byte33's cipher program")
print("02/05/19 V0.1")

upperList = list()
lowerList = list()
newMessageList = list()
newMessage = ""

message = input("Enter your message:\t")
message = message.split()


#The amount to shift
shiftNum = int(input("How much shift?\t"))
shiftDir = input("In what direction? (L/R)\t")


#Make list of uppercase characters
for upper in range(26):
    upperList.append(chr(upper+65))

#Make list of lowercase characters
for lower in range(26):
    lowerList.append(chr(lower+97))

#Main cipher goes here
for word in message:
    letterList = []
    fullWord = ""
    for letter in word:
        if ord(letter) >= 65 and ord(letter) <= 90:
            if shiftDir == "L":
                letterList.append(upperList[(upperList.index(letter)+shiftNum) % 26])
            elif shiftDir == "R":
                letterList.append(upperList[(upperList.index(letter) - shiftNum) % 26])
        elif ord(letter) >= 97 and ord(letter) <= 122:
            if shiftDir == "L":
                letterList.append(lowerList[(lowerList.index(letter)+shiftNum) % 26])
            elif shiftDir == "R":
                letterList.append(lowerList[(lowerList.index(letter) - shiftNum) % 26])

    for finalLetter in letterList:
        fullWord = fullWord + finalLetter
    newMessageList.append(fullWord)

for finalWord in newMessageList:
    newMessage = newMessage + finalWord + " "

print(newMessage)


