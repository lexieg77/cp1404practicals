# odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end = " ")
print()

# a #
for i in range (0, 101, 10):
    print(i, end = ' ')
print()

# b #
for i in range (20, 0, -1):
    print(i, end = ' ')
print()

# c #
number_of_stars = int(input("Please enter a number: "))
for i in range (0, number_of_stars, 1):
    print("*", end = ' ')
print()

# d #
number_of_lines = int(input("Please enter a number: "))
i = 1
while i <= number_of_lines:
    for j in range (0, i, 1):
        print("*", end = ' ')
    print("\n")
    i = i + 1


