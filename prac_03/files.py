# Q1.
user_name = input("Enter your name: ")
out_file = open("name.txt", 'w')
print(user_name, file = out_file)
out_file.close()

# Q2.
out_file = open("name.txt", 'r')
name = out_file.readline().strip()
print(f"Hi {name}!")
out_file.close()

# Q3.
with open("numbers.txt", 'r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    number_addition = first_number + second_number
print(f"The addition of {first_number} and {second_number} is {number_addition}")

# Q4.
total = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)