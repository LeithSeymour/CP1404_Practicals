# x any y input
menu = "E - Even numbers between x and y\nO - Odd numbers between x and y\nS - Squares of x to y\nQ - exit program"
x = int(input("enter a variable for x: "))
y = int(input("enter variable for y: "))
while x > y:
    print("Choose a variable less than", y)
    x = int(input("enter a new variable for x: "))
print(menu)
choice = input("Select a option to run: ").upper()
while choice != "Q":
    if choice == "E":
        if not x % 2 == 0:
            x += 1
        for i in range(x, (y + 1), 2):
            print(i, end=' ')
        print("Are the even numbers between", x, "and", y)
        choice = "Q"
    elif choice == "O":
        while x < y:
            x2 = x
            y2 = y
            x = y2
            y = x2
            if x % 2 == 0:
                x -= 1
            for i in range(x, (y - 2), -2):
                print(i, end=' ')
            print("Are the odd numbers between", x, "and", y)
    elif choice == "S":
        for i in range(x, y):
            squares = [i ** 2]
            print(squares, end=' ')
        print("Are the squares between", x, "and", y)
        choice = "Q"
