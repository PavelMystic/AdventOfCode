import re


def extract_integers(text: str) -> list[str]:
    return re.findall(r"\d+", text)


def line_to_numbers(line: str) -> tuple[int, list[int], list[int]]:
    """Function extracts from the card line the card number, list of winning numbers and list of
    ticket numbers.

    Args:
        line (str): card string

    Returns:
        tuple[int, list[int], list[int]]: extracted data
    """

    card_and_numbers: list[str] = line.split(":")
    assert len(card_and_numbers) == 2, "Wrong card format!"

    card_number_text: list[str] = extract_integers(card_and_numbers[0])
    assert len(card_number_text) == 1, "Wrong card number!"
    card_number: int = int(card_number_text[0])

    numbers: str = card_and_numbers[1]
    winning_and_ticket: list[str] = numbers.split("|")
    assert len(card_and_numbers) == 2, "Wrong numbers format!"

    winning_numbers_text: list[str] = extract_integers(winning_and_ticket[0])
    winning_numbers: list[int] = [int(number) for number in winning_numbers_text]

    ticket_numbers_text: list[str] = extract_integers(winning_and_ticket[1])
    ticket_numbers: list[int] = [int(number) for number in ticket_numbers_text]

    return card_number, winning_numbers, ticket_numbers

def evaluate_matches(winning_numbers: list[int], ticket_numbers: list[int]) -> set[int]:
    return set(winning_numbers).intersection(set(ticket_numbers))

def evaluate_card(winning_numbers: list[int], ticket_numbers: list[int]) -> int:
    """Function assigns points to a card based ont the winning and ticket numbers.

    Args:
        winning_numbers (list[int]): _description_
        ticket_numbers (list[int]): _description_

    Returns:
        int: _description_
    """

    good_numbers: set[int] = evaluate_matches(winning_numbers, ticket_numbers)

    if good_numbers:
        return 2 ** (len(good_numbers) - 1)
    else:
        return 0


def test() -> bool:
    lines: list[str] = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]
    points: list[int] = [8, 2, 2, 1, 0, 0]

    results = [0 for _ in points]

    for line_idx, line in enumerate(lines):
        card_number, winning_numbers, ticket_numbers = line_to_numbers(line)
        print(f"{line} -> {card_number}, {winning_numbers}, {ticket_numbers}")
        results[line_idx] = evaluate_card(winning_numbers, ticket_numbers)


    print(f"{points} -> {results}")
    marks: list[bool] = [point == result for point, result in zip(points, results)]

    return all(marks)


if __name__ == "__main__":
    print(test())

    point_sum: int = 0

    points: list[int] = []
    count: list[int] = []

    with open("./Day_4/input.txt", "r") as file:
        for line in file:
            card_number, winning_numbers, ticket_numbers = line_to_numbers(line)
            points.append(len(evaluate_matches(winning_numbers, ticket_numbers)))
            count.append(1) # one original at the beginning
            point_sum += evaluate_card(winning_numbers, ticket_numbers)

    for card_idx, point in enumerate(points):

        for count_idx in range(count[card_idx]):

            for point_idx in range(point):

                count[card_idx + point_idx + 1] += 1
    

    print(point_sum)
    print(sum(count))