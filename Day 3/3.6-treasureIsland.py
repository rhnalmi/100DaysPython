print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')

print("Welcome to Treasure Island.")
print("Your mission is to find treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". ').lower()

if choice1 == "left":
    # biar ga error dalam penulisan tanda petik satu disuatu kata, Gunakan *\* untuk bikin komputer mengabaikan tanda petik satu tersebut
    choice2 = input('You\'ve come to a lake, There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose? ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the Treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beast. Game Over.") 
        else:
            print("You choose door that doesn't exist. Game Over.")   
    else:
        print("You got attacked by an angry Trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")    