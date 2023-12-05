import random

DIGIT_WORDS: list[tuple[str, int]] = [("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9")]
DIGIT_WORD: dict[str, int] = dict(DIGIT_WORDS)

def line_to_number(line: str) -> int:
    """Function accepts one file line as string, decomposes it to single characters and then select 
    those that are digits. The result is either the first one and the last one, interpreted as a two 
    digit number. If there is no digit in the string, the default result is zero.

    Args:
        line (str): one obfuscated calibration value line

    Returns:
        int: the assumed calibration value
    """
    old_line: str = line
    line_contains_word: bool = True

    while line_contains_word:
        line_contains_word = False
        min_key_idx: int = 1e20
        max_key_idx: int = 0
        first_key: str = ""
        last_key: str = ""

        for key in DIGIT_WORD.keys():
            if key in line:
                line_contains_word = True
                key_idx = line.find(key)
                if key_idx < min_key_idx:
                    min_key_idx = key_idx
                    first_key = key
                if key_idx > max_key_idx:
                    max_key_idx = key_idx
                    last_key = key

        if line_contains_word:
            if len(first_key) > 0:
                line = line.replace(first_key, DIGIT_WORD[first_key])
            if len(last_key) > 0:
                line = line.replace(last_key, DIGIT_WORD[last_key])
        
    digit_list: list[str] = [s for s in list(line) if s.isdigit()]

    if len(digit_list) > 0:
        two_digits: str = digit_list[0] + digit_list[-1]
        return int(two_digits)
    else:
        return 0
    
if __name__ == "__main__":

    sum: int = 0

    with open("./Day_1/input.txt", "r") as file:
        for line in file:
            line_number = line_to_number(line)
            sum += line_number

            if random.random() < 0.1:
                print(f"{line} -> {line_number}")

    print(sum)

    # line_list: list[str] = ["two1nine",
    #     "eightwothree",
    #     "abcone2threexyz",
    #     "xtwone3four",
    #     "4nineeightseven2",
    #     "zoneight234",
    #     "7pqrstsixteen"]
    
    # sum: int = 0

    # for line in line_list:
    #     line_number: int = line_to_number(line)
    #     print(line_number)
    #     sum += line_number

    # print(sum)