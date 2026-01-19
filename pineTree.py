height = int(input("How high do you want your tree to be?"))
for i in range(height, 0, -1):
  for j in range(i):
    print(" ", end=" ")
  for j in range(height - i + 1):
    print("*", end=" ")
  for j in range(height - i):
    print("*", end=" ")
  print("")
for i in range(height, 0, -1):
  print (" ", end=" ")
print("*")