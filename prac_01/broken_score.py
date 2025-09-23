score = float(input("Enter Score: "))

while (score < 0) or (score > 100):
    score = float(input("Please enter a valid score: "))

if (score > 0) and (score < 50):
    print("Bad")
if (score >= 50) and (score < 90):
    print("Passable")
if (score >= 90) and (score <= 100):
    print("Excellent")
