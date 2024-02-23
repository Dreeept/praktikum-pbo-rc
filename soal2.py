grades = {} #inisiasi dict
orang = int(input("n = ")) #input that how many people put in dictionary

for i in range(orang): #looping to input the value of name and grades to dictionary
    keys = input("Name : ") #keys of dictionary
    value = int(input("Grade : ")) #value of the keys
    grades[keys] = value #defining the key with the value to the grade's dictionary
print(f"{grades}, {type(grades)}")