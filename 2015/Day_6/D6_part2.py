import numpy as np

def get_coordinates(line, lights):
    divided = line.split(sep=" ")
    if "on" in divided:
        initial_coordinates = divided[2].split(sep=",")
        final_coordinates = divided[4].split(sep=",")
        lights = turn_on(lights, int(initial_coordinates[0]), int(final_coordinates[0]), int(initial_coordinates[1]), int(final_coordinates[1]))
    elif "off" in divided:
        initial_coordinates = divided[2].split(sep=",")
        final_coordinates = divided[4].split(sep=",")
        lights = turn_off(lights, int(initial_coordinates[0]), int(final_coordinates[0]), int(initial_coordinates[1]), int(final_coordinates[1]))
    elif "toggle" in line:
        initial_coordinates = divided[1].split(sep=",")
        final_coordinates = divided[3].split(sep=",")
        lights = toggle(lights, int(initial_coordinates[0]), int(final_coordinates[0]), int(initial_coordinates[1]), int(final_coordinates[1]))
    return lights

def turn_on(lights, i_row, f_row, i_column, f_column):
    for column in range(i_column, f_column+1):
        for row in range(i_row, f_row+1):
            lights[column][row] += 1 # Change the value of the element
    return lights

def turn_off(lights, i_row, f_row, i_column, f_column):
    for column in range(i_column, f_column+1):
        for row in range(i_row, f_row+1):
            if lights[column][row] > 0:
                lights[column][row] -= 1 # Change the value of the element
    return lights

def toggle(lights, i_row, f_row, i_column, f_column):
    for column in range(i_column, f_column+1):
        for row in range(i_row, f_row+1):
            lights[column][row] += 2
    return lights


input = open("2015/Day_6/input_day6.txt","r")
lights = np.zeros( (1000, 1000) )

for line in input:
    lights = get_coordinates(line, lights)

total_brightness = 0

for i in range(1000):
    for j in range(1000):
        total_brightness += lights[i][j]

print("The total brightness of all lights combined is " + str(total_brightness))
