input = open("2015/Day_3/input_day3.txt","r")

directions = ""
for line in input:
    directions = directions + line

#print(directions)

locations_visited = []
current_location = [0,0]
houses_visited = 0

#directions = "^v^v^v^v^v"

for direction in directions:
    if current_location in locations_visited:
        if direction == "^":
            current_location[1] = current_location[1] + 1
        elif direction == ">":
            current_location[0] = current_location[0] + 1
        elif direction == "v":
            current_location[1] = current_location[1] - 1
        elif direction == "<":
            current_location[0] = current_location[0] - 1
        else:
            print("la dieccion no exisye")
        #print(current_location)
        #print(locations_visited)
    else:
        copy_location = current_location.copy()
        locations_visited.append(copy_location)
        #print(locations_visited)
        if direction == "^":
            current_location[1] = current_location[1] + 1
            houses_visited = houses_visited + 1
            #print(locations_visited)
        elif direction == ">":
            current_location[0] = current_location[0] + 1
            houses_visited = houses_visited + 1
        elif direction == "v":
            current_location[1] = current_location[1] - 1
            houses_visited = houses_visited + 1
        elif direction == "<":
            current_location[0] = current_location[0] - 1
            houses_visited = houses_visited + 1
        else:
            print("la dieccion no exisye")
        #print(current_location)
        #print(locations_visited)
        

input.close()

print("The number of houses that receive at least one present is " + str(houses_visited))