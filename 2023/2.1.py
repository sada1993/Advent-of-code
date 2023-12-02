import os
import re

RED_TOTAL = 12
GREEN_TOTAL = 13
BLUE_TOTAL = 14

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

row = 0
sum = 0
with open(relative_path, 'r') as file:
    for line in file:
        row += 1
        games = re.split(r'[:;]', line)
        games = games[1:]
        games = [parse_set(game) for game in games]
        games_possible = [set[0] <= RED_TOTAL and set[1] <= GREEN_TOTAL and set[2] <= BLUE_TOTAL for set in games]
        games_possible = games_possible.count(False)
        if(games_possible == 0):
            sum = sum + row

print(sum)
        