sizeField = int(input("Enter the size of the field: "))
sizeCross = int(input("Enter the size of the crosses: "))

for i in range(sizeField):
    for j in range(sizeField):
        if (j + i) % sizeCross == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")

for i in range(sizeField):
    for j in range(sizeField):
        if (j - i) % sizeCross == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")

for i in range(sizeField):
    for j in range(sizeField):
        if (j * i) % sizeCross == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
