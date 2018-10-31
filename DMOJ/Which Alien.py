antenna = int(input())
eyes = int(input())

troy = 0
vlad = 0
graeme = 0

if antenna >= 2:
    vlad +=1
    graeme +=1
if antenna >= 3:
    troy += 1
    vlad += 1
if antenna >= 6:
    vlad += 1
if eyes >= 2:
    troy += 1
    vlad +=1
    graeme +=1
if eyes >= 3:
    troy += 1
    vlad +=1
    graeme +=1