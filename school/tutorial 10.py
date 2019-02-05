class Human:
    def __init__(self, name):
        self.age = 0
        self.name = name

    def setName(self, newName):
        self.name = newName

    def getAge(self):
        return self.age

    def haveBirthday(self):
        print("Happy birthday to " + self.name + "!")
        self.age += 1

    def walk(self, steps):
        for i in range(steps):
            print("hi")


class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def xComponent(self):
        return self.x

    def yComponent(self):
        return self.y

    def magnitude(self):
        return(self.x**2 + self.y**2)**0.5


v1 = Vector2D(3, 4)
print(v1.xComponent())
print(v1.yComponent())
print(v1.magnitude())

'''
from random import *
from string import ascii_uppercase as u
file = open("students.txt", "w")
for i in range(100):
    name = "".join(choice(u) for i in range(8))
    num = str(randint(400000000, 400999999))
    credits = randint(30, 40)
    points = str(int(credits * (randint(4,11) + random())))
    file.write(name + "\t" + num + "\t" + str(credits))
    file.write("\t" + points + "\n")
file.close()
'''

class Student:
    def __init__(self, name, number, units, points):
        self.name = name
        self.number = number
        self.units = units
        self.points = points

    def getName(self):
        return self.name

    def getStudentNumber(self):
        return self.number

    def getUnits(self):
        return self.units

    def getPoints(self):
        return self.points

    def gpa(self):
        return self.points/self.units


def main():
    infile = open("students.txt", "r")
    infoString = infile.readline()
    name, number, units, points = infoString.split("\t")
    
    for line in infile:
        name, number, units, points = line.split("\t")
        s = Student(name, number, units, points)
        if s.gpa() > best.gpa():
            best = s
    print("Best GPA is", best.name(), name)