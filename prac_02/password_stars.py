MIN_LENGTH = 8
password = input("Enter a password: ")
while len(password) < MIN_LENGTH:
    print(f"Password must be {MIN_LENGTH} charcaters long")
    password = input("Enter a password: ")

for i in range(len(password)):
    print("*", end = " ")