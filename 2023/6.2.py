import os
import re
import math

script_dir = os.path.dirname(__file__)

relative_path = os.path.join(script_dir, 'inputs', '6.txt')

times = []
distance = []
with open(relative_path, 'r') as file:
    for line in file:
        if re.match(r'^Time', line):
            times = re.findall(r'(\d+)', line)
            times = int(''.join(times))
        elif re.match(r'^Distance', line):
            distance = re.findall(r'(\d+)', line)
            distance = int(''.join(distance))

# if x = time button in pressed
# distance travelled = x * (time - x)
# distance travelled = x*time - x^2
# x^2 - x*time + distance travelled = 0
# x = (time +- sqrt(time^2 - 4*distance travelled))/2

x1 = math.floor((times + (times**2 - 4*distance)**0.5)/2)
x2 = math.ceil((times - (times**2 - 4*distance)**0.5)/2)

print(x1-x2+1)