import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    number_of_quick_picks = int(input("How many quick picks would you like? "))

    for i in range(number_of_quick_picks):
        numbers = []
        for j in range(NUMBERS_PER_LINE + 1):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in numbers:
                numbers.append(number)

        quick_pick = sorted(numbers)


main()
