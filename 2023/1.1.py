import os
import re

script_dir = os.path.dirname(__file__)

relative_path = os.path.join(script_dir, '2023', 'inputs', '1.1.txt')

sum = 0
with open(relative_path, 'r') as file:
    for line in file:
        match_expr = r'(\d)'
        matches = re.findall(match_expr, line)
        first_number = matches[0]
        last_number = matches[-1]
        sum += int(first_number + last_number)
print(sum)
