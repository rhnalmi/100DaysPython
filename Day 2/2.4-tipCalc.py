print("Welcome to tip Calculator.")
bill = input("what was your total bill? $")
percent = input("What percentage tip you would like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

bill_as_float = float(bill)
percent_as_float = float(percent) / 100 + 1
people_as_int = int(people)

total = round((bill_as_float / people_as_int) * percent_as_float, 2)
total = "{:.2f}".format(total)
print(f"Each person should pay: ${total}")
        

#Her Code
#if the bill was $150.00, split between 5 people, with 12% tip
#each person should pay (150.00 / 5) * 1.12 = 33.6
#round the result to 2 decimal places = 33.60

print("\nWelcome to the tip calculator!")
bill_2 = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
people_2 = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100 
total_tip_amount = bill_2 * tip_as_percent
total_bill = bill_2 + total_tip_amount
bill_per_person = total_bill / people_2
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")