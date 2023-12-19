input = open("2015/Day_1/input_day1.txt","r")

complete_input = ""
for line in input:
    complete_input = complete_input + line

floor = 0

position_character = 1
for element in complete_input:
    if element == "(":
        floor = floor + 1
    elif element == ")":
        floor = floor - 1
    if floor == -1:
        print("The position of the first character that causes him to enter the basement is " + str(position_character))

    position_character = position_character + 1

input.close()

print(floor)