input = open("2015/Day_2/input_day2.txt","r")

def calculate_ribbon(length, width, height):
    dimensions = [length, width, height]
    small_side1 = min(dimensions)
    dimensions.remove(small_side1)
    small_side2 = min(dimensions)
    length_ribbon = (2*small_side1) + (2*small_side2)
    return length_ribbon

total_ribbon = 0

for line in input:
    clean_line = line.strip()
    dimensions = clean_line.split(sep="x")
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])
    length_ribbon = calculate_ribbon(length, width, height) + (length*width*height)
    print(length_ribbon)
    total_ribbon = total_ribbon + length_ribbon

input.close()

print("The total total feet of ribbon needed is " + str(total_ribbon))
