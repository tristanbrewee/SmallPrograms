height = float(input("What is your height?"))
weight = float(input("What is your weight?"))

bmi = weight / (height ** 2)

print(round(bmi, 2))