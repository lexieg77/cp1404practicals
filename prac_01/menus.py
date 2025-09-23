name = input("Enter name: ")

# display menu
MENU = """(H)ello
(G)oodbye
(Q)uit
"""

print(MENU)

choice = input("")

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print ("Invalid message")

    # display menu
    print(MENU)
    choice = input("")
print("Finished.")


""" menu string: MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"""
