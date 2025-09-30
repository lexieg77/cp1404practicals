"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
 - The numerator or denominator entered are not integers

2. When will a ZeroDivisionError occur?
 - If the denominator is set to 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
 - Use a while statement to prompt the user to enter a non-zero denominator

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")