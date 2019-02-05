# DO NOT PUT AN INPUT STATEMENT IN THIS CELL

########################---buzz: Check if a given number yields "Buzz" (5 Marks)---########################
def buzz(checkNum, buzzNum):
    stringNum = str(checkNum)
    x = False

    for i in stringNum:
        if int(i) == buzzNum:
            x = True

    if (checkNum % buzzNum == 0) and (checkNum != 0):
        return 'Buzz'
    elif x == True:
        return 'Buzz'
    else:
        return stringNum


###################---whileBuzz: Play Buzz until a given number of "Buzz"s (5 Marks)---####################
def whileBuzz(buzzCount, buzzNum):
    x = 0
    buzzTimes = 0
    finalList = list()

    while (buzzCount > buzzTimes):
        finalList.append(buzz(x, buzzNum))
        if (finalList[-1] == "Buzz"):
            buzzTimes += 1
            x += 1
        else:
            x += 1
    return (finalList)
