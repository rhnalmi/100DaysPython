# TypeError
# len(123)

# no TypeError
len("Hello")

# type checking
print(type("Abc"))
print(type(123))
print(type(3.14))
print(type(True))

# type conversion
str()
int()
float()
bool()

name_of_the_user = input("Enter your name")
lenght_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) #str
print(type(lenght_of_name)) #int

print("Number of letters in your name: " + str(lenght_of_name))