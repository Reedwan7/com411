print("please enter first number")
number_1 = int(input())
print("\n")
print("please enter second number")
number_2 = int(input())
print("\n")
print("please enter third number")
number_3 = int(input())
print("\n")
# Determine the odd numbers
even_numbers = 0
odd_numbers = 0
print("\n")
if number_1 % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
print("\n")
if number_2 % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
print("\n")
if number_3 % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
print("\n")
# Display result
print(f"there were {odd_numbers} odd number and {even_numbers} even number.")



