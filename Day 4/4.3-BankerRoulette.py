# Import the random module 
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_int = random.randint(0,4)

if random_int == 0:
    print(names[0]+" is going to buy the meal today!")
elif random_int == 1:
    print(names[1]+" is going to buy the meal today!")
elif random_int == 2:
    print(names[2]+" is going to buy the meal today!")
elif random_int == 3:
    print(names[3]+" is going to buy the meal today!")
else:
    print(names[4]+" is going to buy the meal today!")

'''
#punya angela

import random

names_string = input("Give me everybody's names, seperated by comma. ")
names = names_string.split(", ")

#get the total number of item in list.
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")

'''