"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def return_score(score):
    while score > 100 or score < 0:
        print("Invalid")
        score = float(input("Enter new score: "))
    if score >= 90:
        category = "Excellent"
    elif score < 50:
        category = "Bad"
    else:
        category = "Passable"
    return category


user_input = float(input("Enter score: "))
result = return_score(user_input)
print(result)
