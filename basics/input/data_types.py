print("what is your name human?")
input()
print("\n")
print("How old are you (in years)?")
whole_number = int(input())
print("\n")
print("How tall are you (in meters)?")
decimal_number = float(input())
print("\n")
print("How much do you weigh (in kilograms)?")
whole_number = int(input())
print("\n")

# calculate bmi
bmi = tall / (weigh ** 2)

#display result
print(f"{name} your bmi is {bmi}")
