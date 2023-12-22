def convert_lower(line):
    new_line = line.lower()
    return new_line

def first_rule(line):
    rule1 = False
    for i in range(len(line)-1):
        if line[i-1] == line[i+1]:
            rule1 = True
    return rule1

def second_rule(line):
    rule2 = False
    substrings = []
    for i in range(len(line)):
        divided = line[i:i+2]
        substrings.append(divided)
    for element in substrings:
        count = substrings.count(element)
        if count > 1:
            index1 = line.find(element)
            index2 = line.find(element,index1 + 1)
            difference = index2 - index1
            if difference >= 2:
                rule2 = True
                break
            elif difference == 1 and element == substrings[index2+1]:
                rule2 = True
    return rule2

strings_nice = 0
input = open("2015/Day_5/input_day5.txt","r")

for line in input:
    lower_line = convert_lower(line)
    if first_rule(line) and second_rule(line):
        strings_nice += 1

print("The number of strings that are nice is " + str(strings_nice))
