import random
import my_module

rand_int = random.randint(1, 10)
print(rand_int)

print(my_module.my_favorite_number)

random_0_to_1 = random.random()
print(random_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

#The Task, my solution

rand_head_or_tails = random.randint(1 ,10)

if rand_head_or_tails % 2 == 0:
    print("Heads")
else:
    print("Tails")