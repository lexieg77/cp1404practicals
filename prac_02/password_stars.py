MIN_LENGTH = 8

def main():
    password = get_password()
    print_astericks(password)

def print_astericks(password):
    for i in range(len(password)):
        print("*", end=" ")

def get_password():
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be {MIN_LENGTH} charcaters long")
        password = input("Enter a password: ")
    return password

main()
