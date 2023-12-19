input = open("2015/Day_2/input_day2.txt","r")

def calculate_surface_area(length, width, height):
    area = (2*length*width) + (2*width*height) + (2*height*length)
    return area

def calculate_smallest_area(length, width, height):
    dimensions = [length, width, height]
    small_side1 = min(dimensions)
    dimensions.remove(small_side1)
    small_side2 = min(dimensions)
    area = small_side1 * small_side2
    return area

paper_needed = 0

for line in input:
    clean_line = line.strip()
    dimensions = clean_line.split(sep="x")
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])
    surface_area = calculate_surface_area(length, width, height)
    small_area = calculate_smallest_area(length, width, height)
    total_area = surface_area + small_area
    #print(total_area)
    paper_needed = paper_needed + total_area

input.close()

print("The total square feet of wrapping paper needed is " + str(paper_needed))
