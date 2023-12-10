"""Solution of the Day 6 assignment."""
from os.path import join
from dataclasses import dataclass
import re
from functools import reduce

@dataclass
class RaceRecord:
    time: int
    distance: int

def extract_integers(text: str) -> list[str]:
    """This function extracts list of integers from string. Each integer should be separated by
    space.

    Args:
        text (str): string of number repsenting characters, numbers separated by spaces

    Returns:
        list[str]: extracted numbers
    """
    return re.findall(r"\d+", text)

def main(file_path: str) -> int:

    races = load_file(file_path)
    result_options: list[int] = []

    for race in races:
        winn_options = winning_options(race)
        result_options.append(len(winn_options))

    return reduce(lambda x, y: x*y, result_options)



def winning_options(race: RaceRecord) -> list[tuple[int, int]]:

    options: list[tuple[int, int]] = []

    for push_time in range(race.time):

        resulting_distance: int = (race.time - push_time)*push_time

        if resulting_distance > race.distance:
            options.append((push_time, resulting_distance))
    
    return options

def load_file(file_path: str) -> list[RaceRecord]:

    times: list[int] = []
    distances: list[int] = []
    
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "Time:" in line:
                times = [int(time_text) for time_text in extract_integers(line.replace("Time:", "").strip())]
            elif "Distance:" in line:
                distances = [int(distance_text) for distance_text in extract_integers(line.replace("Distance", "").strip())]
    
    races = [RaceRecord(time, distance) for time, distance in zip(times, distances)]

    return races


def test(test_file_path: str) -> bool:

    true_options: list[int] = [4, 8, 9]
    result_options: list[int] = []

    races = load_file(test_file_path)

    for race in races:
        winn_options = winning_options(race)
        result_options.append(len(winn_options))

    return all([true_option == result_option for true_option, result_option in zip(true_options, result_options)])




if __name__ == "__main__":

    file_path: str = join(".", "Day_6", "input.txt")
    # file_path: str = join(".", "Day_6", "test.txt")

    print(main(file_path))