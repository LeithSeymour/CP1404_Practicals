"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# if 100 >= score >= 90:
#    print("Excellent")
# elif 90 > score >= 50:
#    print("Passable")
# elif 50 > score > 0:
#    print("Bad")
# else:
#    print("Invalid score")

def return_score(score):
    while score > 100 or score < 0:
        print("Invalid")
        score = float(input("Enter new score: "))
    if score >= 90:
        result = "Excellent"
    elif score < 50:
        result = "Bad"
    else:
        result = "Passable"
    return result


score = float(input("Enter score: "))
result = return_score(score)
print(result)
