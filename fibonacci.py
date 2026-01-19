end = int(input("What is the upper limit?"))
num1 = 0
num2 = 1
print(num1)
print(num2)
while num2 < end:
  num3 = num1 + num2
  num1 = num2
  num2 = num3
  print(num2)