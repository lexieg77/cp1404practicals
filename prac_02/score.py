import random


def main():
    score = float(input("Enter score: "))
    print(determine_score_status(score))
    print("\n")

    # generates a random score and prints the results
    random_score = random.randint(0, 100)
    print(random_score)
    print(determine_score_status(random_score))


def determine_score_status(score):
    """ Determine status from score inputted by the user"""
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
