from prac_07.Guitars import Guitar

print("My Guitars!")
GuitarList = []
flag = True
while flag:
    name = input("Enter Name of Guitar: ")
    if name == "":
        break
    year = int(input("Enter Year of Guitar: "))
    cost = float(input('Enter Cost of Guitar: '))
    details = name, year, cost
    addedGuitar = Guitar(name, year, cost)
    print("{} added".format(addedGuitar))
    GuitarList.append(details)
    Guitar(name, year, cost)

print("These are my Guitars")
for i, guitar in enumerate(GuitarList):
    name, year, cost = guitar
    addedGuitar = Guitar(name, year, cost)
    print("Guitar {}: {}".format(i+1, addedGuitar.pretty_string()))
