year = int(input("Which year you want to check? "))

result = "Leap Year."

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(result)
        else:
            print("Not leap.")
    else:
        print("Not leap.")    
else:
    print("Not leap.")