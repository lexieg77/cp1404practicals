number_of_items = int(input("Number of items: "))
i = 0
total_price_of_all_items = 0

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

while i < number_of_items:
    individual_price_of_each_item = float(input("Price of item: $"))
    i = i + 1
    total_price_of_all_items = total_price_of_all_items + individual_price_of_each_item

if total_price_of_all_items > 100:
    total_price_of_all_items = 0.9*total_price_of_all_items

print(f"Total price for {number_of_items} items is ${total_price_of_all_items:.2f}")

