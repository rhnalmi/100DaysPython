# to use random function, need to import random
import random
#import mymodule

# randint(), tanda kurung tujuannya adalah range angka yang akan dihasilkan
random_integer = random.randint(1,100)
print(random_integer)

# 0.0000000 - 0.9999999999999
random_float = random.random()
#print(random_float)

# ini caranya supaya bisa bikin range float number lebih dari 0,1
rand0m_5 = random_float * 5

print(rand0m_5)

#print(mymodule.pi)