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

score = float(input("Enter score: "))

while score > 100 or score < 0:
    print("Invalid")
    score = float(input("Enter new score: "))

if score >= 90:
    print("Excellent")
elif score < 50:
    print("Bad")
else:
    print("Passable")
