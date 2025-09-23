x = int(input("Enter a number: "))
y = int(input("Enter a bigger number: "))

while x >= y:
    y = int(input("Enter a bigger number please:"))

# display menu
MENU = f"""1. Show the even numbers from {x} to {y}
2. Show the odd numbers from {x} to {y}")
3. Show the squares of the numbers from {x} to {y}
4. Exit the program"""
print(MENU)

choice = input("")

while choice != "4":
    if choice == "1":
        if (x % 2) == 0:
            for i in range (x, y+1, 2):
                print(i, end = " ")
        else:
            for i in range (x+1, y+1, 2):
                print(i, end = " ")
    elif choice == "2":
        if (x % 2) != 0:
            for i in range(x, y+1, 2):
                print(i, end = " ")
        else:
            for i in range(x + 1, y+1, 2):
                print(i, end = " ")
    elif choice == "3":
        for i in range (x, y+1, 1):
            print(i*i, end = " ")
    else:
        print ("Invalid message")

    # display menu
    print("\n")
    print(MENU)

    choice = input("")
print("Finished.")
