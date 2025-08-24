# MY CODEEE
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

low_name1 = name1.lower()
low_name2 = name2.lower()



t1 = low_name1.count("t")
r1 = low_name1.count("r")
u1 = low_name1.count("u")
e1 = low_name1.count("e")

t2 = low_name2.count("t")
r2 = low_name2.count("r")
u2 = low_name2.count("u")
e2 = low_name2.count("e")

l1 = low_name1.count("l")
o1 = low_name1.count("o")
v1 = low_name1.count("v")
ee1 = low_name1.count("e")

l2 = low_name2.count("l")
o2 = low_name2.count("o")
v2 = low_name2.count("v")
ee2 = low_name2.count("e")

true_total = t1 + r1 + u1 +e1 + t2 + r2 +u2 +e2
love_total = l1 + o1 + v1 + ee1 + l2 + o2 + v2 + ee2

score = true_total*10 + love_total

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score <= 50 and score >= 40:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")