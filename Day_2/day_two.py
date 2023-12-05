from functools import reduce
COLOR_NAME_LIST: list[str] = ["red", "green", "blue"]
COLOR_LIMIT_LIST: list[int] = [12, 13, 14]


def validate_game(game_record: str) -> tuple[int, bool, int]:

    game_tuple = tuple(game_record.split(sep=":"))
    assert len(game_tuple) == 2
    game_str = game_tuple[0]
    game_id: int = int(game_str.removeprefix("Game").strip())
    record_str: str = game_tuple[1]
    round_list: list[str] = record_str.split(sep=";")
    game_valid: bool = True
    color_dict: dict[str, int] = {color_name: 0 for color_name in COLOR_NAME_LIST}
    for round in round_list:
        draw_list: list[str] = round.split(sep=",")
        for draw in draw_list:
            for color_name, color_limit in zip(COLOR_NAME_LIST, COLOR_LIMIT_LIST):
                if color_name in draw:
                    color_count: int = int(draw.replace(color_name, "").strip())
                    color_dict[color_name] = max(color_dict[color_name], color_count)
                    
                    if game_valid:
                        game_valid = color_count <= color_limit

                    # it is sufficient to discover one invalid draw
                    # if not game_valid:
                    #     return (game_id, game_valid)
    
    color_power: int = reduce(lambda x, y: x*y, color_dict.values())

    return (game_id, game_valid, color_power)

if __name__ == "__main__":

    game_id, game_valid, color_power = validate_game("Game 3: 16 blue, 2 red, 4 green; 8 red, 4 green; 7 green, 16 blue\n")

    game_id_sum: int = 0
    color_power_sum: int = 0
    with open("./Day_2/input.txt", "r") as file:
        for line in file:
            game_id, game_valid, color_power = validate_game(line)

            # if game_valid:
            #     print(f"{line}: VALID")
            # else:
            #     print(f"{line}: NOT VALID")

            color_power_sum += color_power

            if game_valid:
                game_id_sum += game_id

    print(game_id_sum)
    print(color_power_sum)