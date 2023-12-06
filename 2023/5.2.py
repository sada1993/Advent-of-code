import os
import re

script_dir = os.path.dirname(__file__)

relative_path = os.path.join(script_dir, 'inputs', '5.txt')

def do_mapping(input_vec, map_array):
    output_vec = []
    for i, num in enumerate(input_vec):
        for map in map_array:
            if(num >= map[1] and num < map[1] + map[2]):
                output_vec.append(map[0] + (num - map[1]))
        
        if len(output_vec) != i+1:
            output_vec.append(num)

    return output_vec

def get_seeds(seed_vec):
    output_vec = []
    for num in range(0, len(seed_vec), 2):
        output_vec.extend(list(range(seed_vec[num], seed_vec[num]+seed_vec[num+1])))
    return output_vec


input_vec = []
map_array = []
map_flag = False

with open(relative_path, 'r') as file:
    for line in file:
        if(re.search('seeds', line) != None):
            input_vec = re.findall(r'(\d+)', line)
            input_vec = [int(i) for i in input_vec]
            input_vec = get_seeds(input_vec)
        if map_flag:
            mapping_vec = re.findall(r'(\d+)', line)
            mapping_vec = [int(i) for i in mapping_vec]
            if(len(mapping_vec) != 0):
                map_array.append(mapping_vec)
            else:
                input_vec = do_mapping(input_vec, map_array)
                map_array = []
                map_flag = False 
        if(re.search('map', line) != None):
            map_flag = True     

input_vec = do_mapping(input_vec, map_array)
print('Answer: ', min(input_vec))