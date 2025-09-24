MENU = """
(G)et a valid score 
(P)rint result 
(S)how stars
(Q)uit
"""


def main():
    score = get_valid_score()
    print(MENU)
    choice = input("> ")
    while choice != "Q":
        if choice == "G":  # do I need this ?!
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input("> ")
    print("Farewell")


def get_valid_score():
    """ Get a valid score from the user"""
    score = int(input("Enter a score: "))
    while (score < 0) or (score > 100):
        print("Invalid score!")
        score = int(input("Enter a new score: "))
    return score


def print_result(score):
    """ Print the status reuslts from the score inputted by the user"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def print_stars(score):
    """ Print the score number in asterisks"""
    print("*" * score)


main()
