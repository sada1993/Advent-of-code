import os
import re
import copy

script_dir = os.path.dirname(__file__)

relative_path = os.path.join(script_dir, 'inputs', '25.txt')

def step(direction, position):
    if direction == 'U':
        position[1] += 1
    elif direction == 'D':
        position[1] -= 1
    elif direction == 'L':
        position[0] -= 1
    elif direction == 'R':
        position[0] += 1
    return position

def follow(tail_position, head_position):
    # Function returns [tail_position, steps taken]
    if head_position[0] > tail_position[0]+1 and head_position[1] == tail_position[1]:
        # Right
        tail_position[0] += 1
        return [tail_position, 1]
    if head_position[0] < tail_position[0]-1 and head_position[1] == tail_position[1]:
        # Left
        tail_position[0] -= 1
        return [tail_position, 1]
    if head_position[1] > tail_position[1]+1 and head_position[0] == tail_position[0]:
        # Up
        tail_position[1] += 1
        return [tail_position, 1]
    if head_position[1] < tail_position[1]-1 and head_position[0] == tail_position[0]:
        # Down
        tail_position[1] -= 1
        return [tail_position, 1]
    if (head_position[0] > tail_position[0]+1 and head_position[1] > tail_position[1]) or (head_position[0] > tail_position[0] and head_position[1] > tail_position[1]+1):
        # Top right
        tail_position[0] += 1
        tail_position[1] += 1
        return [tail_position, 1]
    if (head_position[0] < tail_position[0]-1 and head_position[1] > tail_position[1]) or (head_position[0] < tail_position[0] and head_position[1] > tail_position[1]+1):
        # Top left
        tail_position[0] -= 1
        tail_position[1] += 1
        return [tail_position, 1]
    if (head_position[0] > tail_position[0]+1 and head_position[1] < tail_position[1]) or (head_position[0] > tail_position[0] and head_position[1] < tail_position[1]-1):
        # Bottom right
        tail_position[0] += 1
        tail_position[1] -= 1
        return [tail_position, 1]
    if (head_position[0] < tail_position[0]-1 and head_position[1] < tail_position[1]) or (head_position[0] < tail_position[0] and head_position[1] < tail_position[1]-1):
        # Bottom left
        tail_position[0] -= 1
        tail_position[1] -= 1
        return [tail_position, 1]
    else:
        return [tail_position, 0]
    

HEAD = [0,0]
TAIL_positions = [[0,0]]
steps_taken = 0
with open(relative_path, 'r') as file:
    for line in file:
        #print(line, "Head:", HEAD, "Tail:", TAIL)
        line = line.split(' ')
        direction = line[0]
        steps = int(line[1])
        for i in range(steps):
            HEAD = step(direction, HEAD)
            #print(TAIL_positions)
            TAIL, tail_steps = follow(copy.deepcopy(TAIL_positions[-1]), HEAD)
            steps_taken += tail_steps
            TAIL_positions.append(TAIL)
            #print(i, ": ", "Head:", HEAD, "Tail:", TAIL, "Steps:", steps_taken)

tuple_list = [tuple(lst) for lst in TAIL_positions]

unique_list_of_lists = [list(tpl) for tpl in set(tuple_list)]

print(len(unique_list_of_lists))
