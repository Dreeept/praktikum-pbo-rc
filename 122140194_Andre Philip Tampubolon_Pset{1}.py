height = int(input("Height = "))
for i in range(height):
    for j in range(i, height, 1): #bikin segitiga siku-siku kosong di bagian kiri
        print(" ", end="")

    for k in range(-1,i,1): #bikin segitiga siku-siku untuk bagian kiri dari segitiga sama kaki
        print("*", end="")

    for l in range(0,i,1): #bikin segitiga siku-siku untuk bagian kanan dari segitiga sama kaki
        print("*", end="")
    else:
        print(" ")
