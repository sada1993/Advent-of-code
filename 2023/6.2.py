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
            times = [int(''.join(times))]
        elif re.match(r'^Distance', line):
            distance = re.findall(r'(\d+)', line)
            distance = [int(''.join(distance))]

answers = []
for time, distance in zip(times, distance):
    for tick in range(1, int(time)+1):
        print(tick)
        epoch_distance = tick * 1 * (time - tick)
        if epoch_distance > distance:
            answers.append(epoch_distance)


print(len(answers))
