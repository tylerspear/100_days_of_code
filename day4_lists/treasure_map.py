row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
treasure_map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
choice = input("Where do you want to put the treasure? (separate by a ','): ")
location = choice.split(',')
vertical = int(location[0]) - 1
horizontal = int(location[1]) - 1

treasure_map[horizontal][vertical] = 'X'
print(f"{row1}\n{row2}\n{row3}")


