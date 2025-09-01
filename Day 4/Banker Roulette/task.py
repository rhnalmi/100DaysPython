import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


#1st opt
pay_the_bill = random.randint(0, 4)
print(friends[pay_the_bill])

#2nd Opt
pay_bill = random.choice(friends)
print(pay_bill)