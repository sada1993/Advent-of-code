import os
import re
from functools import reduce
import operator

script_dir = os.path.dirname(__file__)

relative_path = os.path.join(script_dir, 'inputs', '6.txt')

times = []
distance = []
with open(relative_path, 'r') as file:
    for line in file:
        if re.match(r'^Time', line):
            times = re.findall(r'(\d+)', line)
            times = [int(x) for x in times]
        elif re.match(r'^Distance', line):
            distance = re.findall(r'(\d+)', line)
            distance = [int(x) for x in distance]

answers = []
for time, distance in zip(times, distance):
    distance_vec = []
    for tick in range(1, int(time)+1):
        distance_vec.append(tick * 1 * (time - tick))
    return_vec = [x for x in distance_vec if x > distance]
    answers.append(len(return_vec))


print(reduce(operator.mul, answers))
