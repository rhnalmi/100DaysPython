bill = float(input("Berapa total bill? $"))
tip = int(input("berapa tip yang mau diberikan? 10 12 15? "))
people = int(input("jumlah orang split bill: "))

tip_percentage = tip / 100
total_tip_amount = bill * tip_percentage

total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

total = round(bill_per_person, 2)
total = "{:.2f}".format(bill_per_person)

print(f"Total yang harus dibayarkan per orang adalah: ${total}")