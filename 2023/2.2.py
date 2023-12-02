import os
import re

script_dir = os.path.dirname(__file__)
relative_path = os.path.join(script_dir, 'inputs', '2.txt')

def parse_set(set):
    #red, green, and blue
    my_set = [0,0,0]
    red = re.findall(r'(\d+) red', set)
    green = re.findall(r'(\d+) green', set)
    blue = re.findall(r'(\d+) blue', set)
    if(red != []):
        my_set[0] = int(red[0])
    if(green != []):
        my_set[1] = int(green[0])
    if(blue != []):
        my_set[2] = int(blue[0])
    return my_set

sum = 0
with open(relative_path, 'r') as file:
    for line in file:
        games = re.split(r'[:;]', line)
        games = games[1:]
        games = [parse_set(game) for game in games]
        reds = max([set[0] for set in games])
        green = max([set[1] for set in games])
        blue = max([set[2] for set in games])
        sum = sum + (reds * green * blue)

print(sum)

        