"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))

while 0 < score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))

if score > 50:
    print("Passable")
elif score > 90:
    print("Excellent")
else:
    print("Bad")

#Any score under 50 will trigger "Bad" response

