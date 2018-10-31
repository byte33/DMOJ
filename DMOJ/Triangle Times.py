angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
equil = 0
error = 0

if angle1+angle2+angle3 != 180:
    print("Error")
    error = 1

if error == 0:
    if angle1 == angle2 and angle1 == angle3:
        print("Equilateral")
        equil = 1

    if angle1 == angle2 or angle2 == angle3 or angle3 == angle1:
        if equil == 0:
            print("Isosceles")
    else:
        print("Scalene")
