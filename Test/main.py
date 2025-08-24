def main():
    num = [5,3,1]
    for i in num:
        print(''.join(str(x) for x in range(1, i + 1)))
        print('+' * (i-1))

main()

def add_func():
    num = [1,3,5]
    for i in range(len(num)):
        print('+'.join(str(num[x]) for x in range(i + 1)))

add_func()

#python