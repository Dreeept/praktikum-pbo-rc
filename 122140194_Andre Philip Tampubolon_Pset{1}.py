height = int(input("Height = "))
for i in range(height):
    for j in range(i, height, 1):
        print(" ", end="")

    for k in range(-1,i,1):
        print("*", end="")

    for l in range(0,i,1):
        print("*", end="")
    else:
        print(" ")
