numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0]) # 3
print(numbers[-1]) # 2
print(numbers[3]) # 1
print(numbers[:-1]) # [3, 1, 4, 1, 5, 9]
print(numbers[3:4]) # [1, 5] x [1]
print(5 in numbers) # True
print(7 in numbers) # False
print("3" in numbers) # False
print(numbers + [6, 5, 3]) # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# change the first element to "ten"
numbers[0] = "ten"
print(numbers)

# change the last number to 1
numbers[-1] = 1
print(numbers)

# print all but the first two elements
print(numbers[2:])

# print whether 9 is an element of numbers
print(9 in numbers)

