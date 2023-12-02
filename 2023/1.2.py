import os
import re

lookup = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
          'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

merged_string = '|'.join(lookup.keys())

script_dir = os.path.dirname(__file__)

relative_path = os.path.join(script_dir, '2023', 'inputs', '1.1.txt')

sum = 0
with open(relative_path, 'r') as file:
    for line in file:
        line = line.strip()
        match_expr = r'('+merged_string+r'|\d)'
        match_expr_reverse = r'('+merged_string[::-1]+r'|\d)'
        matches = re.findall(match_expr, line)
        matches_reverse = re.findall(match_expr_reverse, line[::-1])

        first_number = matches[0]
        last_number = matches_reverse[0][::-1]
        if(re.search(r'\d', first_number) == None):
            first_number = lookup[first_number]
        if(re.search(r'\d', last_number) == None):
            last_number = lookup[last_number]

        sum += int(first_number + last_number)
print(sum)
