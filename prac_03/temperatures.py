"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Lindsay Ward'


def main():
    menu = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print("{} Celsius is equal to {} Fahrenheit".format(celsius, celsius_to_fahrenheit(celsius)))
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            print("{} Fahrenheit is equal to {} Celsius".format(fahrenheit, fahrenheit_to_celsius(fahrenheit)))
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
