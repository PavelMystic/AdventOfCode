symbol_set: set[str] = set()

lines: list[str] = []

with open("./Day_3/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        lines.append(line)
        

for line in lines:
    char_list = list(line)

    for char in char_list:

        # symbol je cokoli co neni tecka nebo cislo
        if not ("." in char) and not char.isdigit():
            symbol_set.add(char)

print(symbol_set)

symbol_positions: list[tuple[int, int, str, int]] = []
number_positions: list[tuple[int, list[int], list[str]], list[bool]] = []
symbol_id: int = 0

for line_idx, line in enumerate(lines):
    line_chars: list[str] = list(line)

    digit_positions: list[tuple[int, int, str]] = []

    for char_idx, char in enumerate(line_chars):
        if char in symbol_set:
            symbol_id += 1
            symbol_positions.append((line_idx, char_idx, char, symbol_id))
        if char.isdigit():
            digit_positions.append((line_idx, char_idx, char))
    
    for digit_idx, digit_position in enumerate(digit_positions):
        if digit_idx == 0:
            number_positions.append((digit_position[0], [digit_position[1]], [digit_position[2]], [False]))
        else:
            if digit_position[1] - number_positions[-1][1][-1] == 1: # cisla nasleduji
                number_positions[-1][1].append(digit_position[1])
                number_positions[-1][2].append(digit_position[2])
            else:
                number_positions.append((digit_position[0], [digit_position[1]], [digit_position[2]], [False]))
    
symbol_number_relation = {}

for number_position in number_positions:
    neighbor_symbol_positons = [symbol_position for symbol_position in symbol_positions if abs(symbol_position[0] - number_position[0]) <= 1]
    
    for symbol_positon in neighbor_symbol_positons:
        if symbol_positon[1] <= (max(number_position[1]) + 1) and symbol_positon[1] >= (min(number_position[1]) - 1):
            if symbol_positon[3] in symbol_number_relation:
                symbol_number_relation[symbol_positon[3]].append(number_position)
            else:
                symbol_number_relation[symbol_positon[3]] = [number_position]

            number_position[3][0] = True

number_list = [int("".join(number_position[2])) for number_position in number_positions if number_position[3][0]]
print(sum(number_list))

gear_sum = 0

for key, value in symbol_number_relation.items():
    if len(value) == 2:
        symbol = [symbol_positon for symbol_positon in symbol_positions if key == symbol_positon[3]]

        if "*" in symbol[0][2]:
            gear_prod: int = 1
            for number_position in value:
                gear_prod *= int("".join(number_position[2]))
            
            gear_sum += gear_prod

print(gear_sum)
