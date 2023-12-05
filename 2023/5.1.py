import os
import re

script_dir = os.path.dirname(__file__)

relative_path = os.path.join(script_dir, 'inputs', '5.txt')

def create_map(map, mapping_vec):
    for i in range(mapping_vec[2]):
        map[mapping_vec[1] + i] = mapping_vec[0] + i

def do_mapping(input_vec, map):
    output_vec = []
    for i in input_vec:
        if i in map:
            output_vec.append(map[i])
        else:
            output_vec.append(i)
    return output_vec


input_vec = []
map_array = []
map_flag = False
map = {}

counter = 0
with open(relative_path, 'r') as file:
    for line in file:
        if(re.search('seeds', line) != None):
            input_vec = re.findall(r'(\d+)', line)
            input_vec = [int(i) for i in input_vec]
        if map_flag:
            mapping_vec = re.findall(r'(\d+)', line)
            mapping_vec = [int(i) for i in mapping_vec]
            if(len(mapping_vec) != 0):
                #print("mapping_vec:", mapping_vec)
                create_map(map, mapping_vec)
            else:
                input_vec = do_mapping(input_vec, map)
                map = {}
                map_flag = False 
                #print("post mapping input_vec:", input_vec)
            #print(map)
        if(re.search('map', line) != None):
            map_flag = True     

input_vec = do_mapping(input_vec, map)
print('Answer: ', min(input_vec))