"""This script implements the solution of the Day 7 challenge of the 2023 Advent of Code."""

from os.path import join
from functools import cmp_to_key

# TODO card strength evaluationw without hadnd writing, e.g. digits are less than letters (then digits can be converted and compared) and fow letter perhaps ascii or something?
CARD_STRENGTH: dict[str, int] = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
    "J": -1,
}
CardHist = dict[str, int]


def main(main_file_name: str) -> int:
    """Main processing function.

    Args:
        main_file_name (str): main data file name

    Returns:
        int: total winnings
    """

    hand_bids: dict[str, int] = {}

    with open(main_file_name, "r", encoding="utf-8") as file:
        for line in file:
            line_parts: list[str] = line.split(" ")
            hand_bids[line_parts[0]] = int(line_parts[1])

    hand_list: list[str] = list(hand_bids.keys())
    hand_list = sorted(hand_list, key=cmp_to_key(compare_hands), reverse=True)

    total_winnings: int = 0

    for hand_idx, hand in enumerate(hand_list):
        total_winnings += hand_bids[hand] * (len(hand_list) - hand_idx)
    return total_winnings


def get_type(hand: str) -> int:
    """Function evaluates the hand type.

    Args:
        hand (str): hand description

    Returns:
        int: hand type, the higher, the better
    """

    card_hist: CardHist = {}

    for card in list(hand):
        if card in card_hist:
            card_hist[card] += 1
        else:
            card_hist[card] = 1

    card_hist = apply_jokers(card_hist)

    if is_five_of_a_kind(card_hist):
        return 6
    if is_four_of_a_kind(card_hist):
        return 5
    if is_full_house(card_hist):
        return 4
    if is_three_of_a_kind(card_hist):
        return 3
    if is_two_pair(card_hist):
        return 2
    if is_one_pair(card_hist):
        return 1

    return 0


def is_five_of_a_kind(card_hist: CardHist) -> bool:
    """Function evaluated whether the hand is five of a kind based on the card histogram.

    Args:
        card_hist (CardHist): dictionary of card name and its count in hand (only card that
        are actually in the hand)

    Returns:
        bool: is the hand five of a kind
    """
    kind_count: int = 5
    return kind_count in card_hist.values()


def is_four_of_a_kind(card_hist: CardHist) -> bool:
    """Function evaluated whether the hand is four of a kind based on the card histogram.

    Args:
        card_hist (CardHist): dictionary of card name and its count in hand (only card that
        are actually in the hand)

    Returns:
        bool: is the hand four of a kind
    """

    kind_count: int = 4
    return kind_count in card_hist.values()


def is_full_house(card_hist: CardHist) -> bool:
    """Function evaluated whether the hand is full house based on the card histogram.

    Args:
        card_hist (CardHist): dictionary of card name and its count in hand (only card that
        are actually in the hand)

    Returns:
        bool: is the hand full house
    """

    return 3 in card_hist.values() and 2 in card_hist.values()


def is_three_of_a_kind(card_hist: CardHist) -> bool:
    """Function evaluated whether the hand is three of a kind based on the card histogram.

    Args:
        card_hist (CardHist): dictionary of card name and its count in hand (only card that
        are actually in the hand)

    Returns:
        bool: is the hand three of a kind
    """

    kind_count: int = 3
    return kind_count in card_hist.values()


def is_two_pair(card_hist: CardHist) -> bool:
    """Function evaluated whether the hand is two pair based on the card histogram.

    Args:
        card_hist (CardHist): dictionary of card name and its count in hand (only card that
        are actually in the hand)

    Returns:
        bool: is the hand two pair
    """

    return sum((elem == 2 for elem in card_hist.values())) == 2


def is_one_pair(card_hist: CardHist) -> bool:
    """Function evaluated whether the hand is one pair based on the card histogram.

    Args:
        card_hist (CardHist): dictionary of card name and its count in hand (only card that
        are actually in the hand)

    Returns:
        bool: is the hand one pair
    """

    return sum((elem == 2 for elem in card_hist.values())) == 1


def apply_jokers(card_hist: CardHist) -> CardHist:
    """This function modifies the card histogram in such a way, that if there are some jokers in the
    hand, they are used to enhance it so that the type is as high as possible.

    Args:
        card_hist (CardHist): dictionary of card name and its count in hand (only card that
        are actually in the hand)
    Returns:
        CardHist: modified card histogram
    """

    if "J" not in card_hist.keys():
        return card_hist

    n_jokers: int = card_hist["J"]

    if n_jokers == 5:
        return card_hist

    max_count: int = max((card_hist[key] for key in card_hist.keys() if "J" not in key))

    max_cards: list[str] = [
        key
        for key in card_hist.keys()
        if card_hist[key] == max_count and "J" not in key
    ]
    max_cards = sorted(max_cards, key=lambda x: CARD_STRENGTH[x])

    card_hist[max_cards[0]] += n_jokers
    del card_hist["J"]

    return card_hist


def compare_hands(first_hand: str, second_hand: str) -> int:
    """Function compares the two hands provided.

    Args:
        first_hand (str): hand description
        second_hand (str): another hand description

    Returns:
        int: 0 if hands are equal, 1 if the first one is more valuable, -1 otherwise
    """

    first_type: int = get_type(first_hand)
    second_type: int = get_type(second_hand)

    if first_type > second_type:
        return 1
    if second_type > first_type:
        return -1

    for first_card, second_card in zip(list(first_hand), list(second_hand)):
        if CARD_STRENGTH[first_card] > CARD_STRENGTH[second_card]:
            return 1
        if CARD_STRENGTH[second_card] > CARD_STRENGTH[first_card]:
            return -1
    return 0


def test(test_file_name: str) -> bool:
    """Test function based on the example imput provided with the assignment.

    Returns:
        bool: test success
    """

    expected_total_winnings: int = 6440
    total_winnings: int = main(test_file_name)

    return total_winnings == expected_total_winnings


if __name__ == "__main__":
    # file_name: str = join("./Day_7/test.txt")
    file_name: str = join("./Day_7/input.txt")

    print(main(file_name))
