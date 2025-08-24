#my code:
age = input("What is your age? ")

x = (90 - int(age)) * 365
y = (90 - int(age)) * 52
z = (90 - int(age)) * 12

print(f"\nYou have {x} days, {y} weeks, and {z} months left.")

#her code:
print("======================")
age = input("What is your age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} left."

print(message)