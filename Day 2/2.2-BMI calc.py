#my code:

height = int(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

bmi = weight / height ** 2

print("Your BMI is: ", bmi)

print("===========================")

# Her code:
height = input("Enter you height in m: ")
weight = input("Enter your weight in Kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)