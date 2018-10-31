length = int(input())

bigList = list()

for i in range(length):
    index = int(input())
    bigList.append(index)

bigList.sort()

for x in bigList:
    print(x)
