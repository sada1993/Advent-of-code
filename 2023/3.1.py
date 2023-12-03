import os
import re

script_dir = os.path.dirname(__file__)
relative_path = os.path.join(script_dir, 'inputs', '3.txt')

def find_number(matrix, i, j, traversed):
    number = [matrix[i][j]]
    traversed_idx = j
    left = j-1
    while(left >= 0 and re.search(r'\d',matrix[i][left]) != None):
        number.insert(0, matrix[i][left])
        traversed_idx = left
        left -= 1
    right = j+1
    while(right < len(matrix[0]) and re.search(r'\d',matrix[i][right]) != None):
        number.append(matrix[i][right])
        right += 1

    traversed_idx = (i,traversed_idx)
    number = int(''.join(number))
    if(traversed_idx not in traversed):
        traversed.append(traversed_idx)
        return [number, traversed]
    else:
        return [None, traversed]

def find_adjacent_numbers(matrix, i, j, traversed):
    #       up        down    left      right   upleft   upright   downleft  downright
    check = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1),  (1, -1),  (1, 1)]
    adjacent_numbers = []
    for (x,y) in check:
        if(i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])):
            if(re.search(r'\d', matrix[i+x][j+y]) != None):
                number, traversed = find_number(matrix, i+x, j+y, traversed)
                adjacent_numbers.append(number)
    adjacent_numbers = [i for i in adjacent_numbers if i is not None]
    return [adjacent_numbers, traversed]
    


# Populate a 2d martix with the input
matrix = []
number = []
traversed = []
with open(relative_path, 'r') as file:
    for line in file:
        line_char = []
        for char in line:
            if(char == '\n'):
                break
            line_char.append(char)
        matrix.append(line_char)

for i,line in enumerate(matrix):
    for j,char in enumerate(line):
        if(re.search(r'[^\d\.]', char) != None):
            [num, traversed] = find_adjacent_numbers(matrix, i, j, traversed)
            number.append(num)

flattened_list = [item for sublist in number for item in sublist]
print(sum(flattened_list))
