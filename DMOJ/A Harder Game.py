amount = int(input())
stuff = input()
stuffList = stuff.split(" ")
increment = 0
personCount = 0
bruce = 0
player = 0

for x in stuffList:
    x = int(x)
    stuffList[increment] = x
    increment += 1

length = round(amount/2)

for i in range(int(amount)):
    first = stuffList[0]
    last = stuffList[-1]
    if first > last:
        if (personCount % 2) == 0:
            player += first
            del stuffList[0]
        else:
            bruce += first
            del stuffList[0]
    elif last > first:
        if (personCount % 2) == 0:
            player += last
            del stuffList[-1]
        else:
            bruce += first
            del stuffList[-1]
    else:
        if (personCount % 2) == 0:
            player += last
            del stuffList[0]
        else:
            bruce += first
            del stuffList[0]
    personCount += 1
print(player)