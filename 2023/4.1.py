import os
import re

script_dir = os.path.dirname(__file__)

relative_path = os.path.join(script_dir, 'inputs', '4.txt')

total_points = 0
with open(relative_path, 'r') as file:
    for line in file:
        parsed_line = re.search(r':(.*)\|(.*)', line)
        winning_numbers = parsed_line.group(1).strip()
        my_numbers = parsed_line.group(2).strip()

        winning_numbers = re.sub(r' +', ' ', winning_numbers).split(' ')
        my_numbers = re.sub(r' +', ' ', my_numbers).split(' ')

        points = 0
        for i, number in enumerate(my_numbers):
            if number in winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        total_points += points

print(total_points)