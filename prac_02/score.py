"""
Program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    print(determine_score_status(score))

def determine_score_status(score):
    if score < 0 or score > 100:
        status = "Invalid score"
    elif score >= 90:
        status = "Excellent"
    elif score >= 50:
        status = "Passable"
    else:
        status = "Bad"
    return status

main()