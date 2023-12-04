def line_to_number(line: str) -> int:
    digit_list: list[int] = [s for s in list(line) if s.isdigit()]

    if len(digit_list) > 0:
        two_digits: str = digit_list[0] + digit_list[-1]
        return int(two_digits)
    else:
        return 0
    
if __name__ == "__main__":

    sum: int = 0

    with open("./Day_1/input.txt", "r") as file:
        for line in file:
            sum += line_to_number(line)

    print(sum)
