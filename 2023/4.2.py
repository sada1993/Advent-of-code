import os
import re

script_dir = os.path.dirname(__file__)

relative_path = os.path.join(script_dir, 'inputs', '4.txt')

my_cards = [1 for i in range(203)] #203 lines in the input file

with open(relative_path, 'r') as file:
    for line in file:
        parsed_line = re.search(r'Card +(\d+):(.*)\|(.*)', line)
        card_number = int(parsed_line.group(1).strip())
        winning_numbers = parsed_line.group(2).strip()
        my_numbers = parsed_line.group(3).strip()

        winning_numbers = re.sub(r' +', ' ', winning_numbers).split(' ')
        my_numbers = re.sub(r' +', ' ', my_numbers).split(' ')

        additional_cards = 0
        for number in my_numbers:
            if number in winning_numbers:
                additional_cards += 1
                idx = card_number - 1 + additional_cards
                for j in range(my_cards[card_number - 1]):
                    my_cards[idx] += 1

print(sum(my_cards))
                