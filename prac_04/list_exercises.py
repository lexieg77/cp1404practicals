numbers = []

# 1. Basic list operations
for i in range(5):
    user_input = int(input("Number: "))
    numbers.append(user_input)
print(numbers)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {(sum(numbers) / len(numbers))}")

# 2. Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")

# 3. Extend basic list operations
i = 1
user_input = int(input(f"Number {i}: "))
while user_input != 0:
    numbers.append(user_input)
    i = i + 1
    user_input = int(input(f"Number {i}: "))
print(numbers)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {(sum(numbers) / len(numbers))}")

# 4. Indefinite set of strings
set_of_strings = []
repeated_strings = []
user_input = input("Enter a string: ")
while user_input != "":
    set_of_strings.append(user_input)
    user_input = input("Enter a string: ")

for item in set_of_strings:
    if set_of_strings.count(item) > 1 and item not in repeated_strings:
        repeated_strings.append(item)
print(repeated_strings)


# 5. Memberwise Addition
def main():
    first_list_of_numbers = [int(x.strip()) for x in input("Enter the first list of numbers: ").split(",")]
    second_list_of_numbers = [int(x.strip()) for x in input("Enter the second list of numbers: ").split(",")]

    result = add_memberwise(first_list_of_numbers, second_list_of_numbers)
    print(result)


def add_memberwise(first_list_of_numbers, second_list_of_numbers):
    """Takes two lists and returns the list that contains the sum of elements in the same index."""
    memberwise_list = []

    # Determine the length of the shorter list
    length = min(len(first_list_of_numbers), len(second_list_of_numbers))

    # Add elements at corresponding indices
    for i in range(length):
        memberwise_addition = first_list_of_numbers[i] + second_list_of_numbers[i]
        memberwise_list.append(memberwise_addition)

    if len(first_list_of_numbers) > len(second_list_of_numbers):
        for number in first_list_of_numbers[length:]:
            memberwise_list.append(int(number))
    else:
        for number in second_list_of_numbers[length:]:
            memberwise_list.append(int(number))

    return memberwise_list


main()
