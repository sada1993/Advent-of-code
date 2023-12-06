import os
import re

script_dir = os.path.dirname(__file__)

relative_path = os.path.join(script_dir, 'inputs', '5.txt')

def do_mapping(input_vec, map_array):
    output_vec = []
    for i in range(0, len(input_vec), 2):
        for map in map_array:
            if(input_vec[i] >= map[1] and input_vec[i]+input_vec[i+1] < map[1] + map[2]):
                #Range is contained in map so no need to split
                output_vec.extend([map[0] + (input_vec[i] - map[1]), input_vec[i+1]])
            elif(input_vec[i] < map[1] and input_vec[i]+input_vec[i+1] > map[1] + map[2]):
                #Range is larger than map so split into three
                output_vec.extend([input_vec[i], map[1] - input_vec[i], map[0], map[2], map[1] + map[2], input_vec[i+1] - (map[1] - input_vec[i] + map[2])])
            elif(input_vec[i] < map[1] and input_vec[i]+input_vec[i+1]-1 < map[1] + map[2]):
                #Range overlaps the map on the lhs so split into two
                output_vec.extend([input_vec[i], map[1] - input_vec[i], map[0], input_vec[i+1] - (map[1] - input_vec[i])])
            elif(input_vec[i] >= map[1] and input_vec[i]+input_vec[i+1]-1 > map[1] + map[2]):
                #Range overlaps the map on the rhs so split into two
                output_vec.extend([map[0] + (input_vec[i] - map[1]), map[1] + map[2] - input_vec[i], map[2], input_vec[i+1] - (map[1] + map[2] - input_vec[i])])
            else:
                output_vec.extend([input_vec[i], input_vec[i+1]])
    return output_vec

#### Unit Tests ####
#All Contained
# print("input:5-15, mapping:0-19 -> 25-44)")
# print("expected: [30,11]")
# print(do_mapping([5, 11], [[25, 0, 20]]))

# print("input:5-15, mapping:6-7 -> 25-26)")
# print("expected: [5,1,25,2,8,8]")
# print(do_mapping([5, 11], [[25, 6, 2]]))

# print("input:5-15, mapping:0-6 -> 25-31)")
# print("expected: [30,2,7,9]")
# print(do_mapping([5, 11], [[25, 0, 7]]))

# print("input:5-15, mapping:14-16 -> 25-27)")
# print("expected: [5,9,25,2]")
# print(do_mapping([5, 11], [[25, 14, 2]]))

# print("Out of Range")
# print("expected: [5,11]")
# print(do_mapping([5, 11], [[25, 20, 100]]))

# print("Out of Range")
# print("expected: [5,11]")
# print(do_mapping([5, 11], [[25, 0, 5]]))

input_vec = []
map_array = []
map_flag = False

with open(relative_path, 'r') as file:
    for line in file:
        if(re.search('seeds', line) != None):
            input_vec = re.findall(r'(\d+)', line)
            input_vec = [int(i) for i in input_vec]
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