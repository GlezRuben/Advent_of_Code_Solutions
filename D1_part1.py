input = open("2015/Day_1/input_day1.txt","r")

complete_input = ""
for line in input:
    complete_input = complete_input + line

floor = 0

for element in complete_input:
    if element == "(":
        floor = floor + 1
    elif element == ")":
        floor = floor - 1

input.close()

print(floor)