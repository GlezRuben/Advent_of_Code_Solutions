def convert_lower(line):
    new_line = line.lower()
    return new_line

def first_rule(line):
    rule1 = False
    vowels = ["a", "e", "i", "o", "u"]
    number_of_vowels = 0
    for letter in line:
        if letter in vowels:
            number_of_vowels += 1
    if number_of_vowels >= 3:
        rule1 = True
    return rule1

def second_rule(line):
    rule2 = False
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            rule2 = True
    return rule2

def third_rule(line):
    rule3 = True
    substrings = ["ab", "cd", "pq", "xy"]
    for i in range(len(line)-1):
        divided = line[i:i+2]
        #print(divided)
        if divided in substrings:
            rule3 = False
    return rule3

strings_nice = 0

input = open("2015/Day_5/input_day5.txt","r")

for line in input:
    is_nice = True
    lower_line = convert_lower(line)
    rule1 = first_rule(line)
    rule2 = second_rule(line)
    rule3 = third_rule(line)

    if rule1 and rule2 and rule3:
        strings_nice += 1

print("The number of strings that are nice is " + str(strings_nice))
