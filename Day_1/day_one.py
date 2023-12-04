def line_to_number(line: str) -> int:
    """Function accepts one file line as string, decomposes it to single characters and then select 
    those that are digits. The result is either the first one and the last one, interpreted as a two 
    digit number. If there is no digit in the string, the default result is zero.

    Args:
        line (str): one obfuscated calibration value line

    Returns:
        int: the assumed calibration value
    """
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
