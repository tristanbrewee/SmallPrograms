height = float(input("What is your height?"))
weight = float(input("What is your weight?"))

bmi = weight / (height ** 2)

print(round(bmi, 2))

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal")
else:
    print("You are overweight")

