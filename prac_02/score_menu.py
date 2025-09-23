MENU = """
(G)et a valid score 
(P)rint result 
(S)how stars
(Q)uit
"""

def main():
    print(MENU)
    choice = input("> ")
    while choice != "Q":
        if choice == "G":
            get_valid_score()
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input("> ")
    print("Farewell")

def get_valid_score():
    score = int(input("Enter a score: "))
    while (score < 0) or (score > 100):
        print("Invalid score!")
        score = int(input("Enter a new score: "))
    return score

main()
