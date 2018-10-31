weight = float(input())
height = float(input())

bmi = 0
bmi = weight/(height**2)

if bmi > 25.0:
    print("Overweight")
elif bmi >= 18.5 and bmi <=25.0:
    print("Normal weight")
elif bmi < 18.5:
    print("Underweight")
