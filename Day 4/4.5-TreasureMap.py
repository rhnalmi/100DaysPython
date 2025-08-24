row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

t = str("X")
if position == "11":
    map[0][0] = t
elif position == "12":
    map[1][0] = t
elif position == "13":
    map[2][0] = t
elif position == "21":
    map[0][1] = t
elif position == "22":
    map[1][1] = t
elif position == "23":
    map[2][1] = t
elif position == "31":
    map[0][2] = t
elif position == "32":
    map[1][2] = t
elif position == "33":
    map[2][2] = t




print(f"{row1}\n{row2}\n{row3}")



#Angela code:
'''
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")
'''

