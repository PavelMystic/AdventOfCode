"""Implementation of the Day 8 assignment."""

from os.path import join
from itertools import cycle

START_NODE: str = "AAA"
END_NODE: str = "ZZZ"
LR_DICT: dict[str, int] = {"L": 0, "R": 1}


def node_to_lr(node: str) -> tuple[str, tuple[str, ...]]:
    node_parts: list[str] = node.split(" = ")
    assert len(node_parts) == 2, "Wrong node format!"

    node_parts[1] = node_parts[1].replace("(", "").replace(")", "")
    lr_part: list[str] = node_parts[1].split(", ")

    return node_parts[0], tuple(lr_part)


def main(main_file_name: str) -> int:
    """Main processing function of this script.

    Args:
        main_file_name (str): full main file path

    Returns:
        int: number of steps required to get from AAA to ZZZ
    """

    node_map: dict[str, tuple[str, str]] = {}

    with open(main_file_name, "r", encoding="utf-8") as file:
        for line_idx, line in enumerate(file):
            if line_idx == 0:
                instructions: str = line.strip()
            if line_idx >= 2:
                node_name, lr_part = node_to_lr(line.strip())
                node_map[node_name] = lr_part

    current_node: str = START_NODE
    step_count: int = 0

    for instruction in cycle(instructions):
        current_node = node_map[current_node][LR_DICT[instruction]]
        step_count += 1

        if current_node == END_NODE:
            return step_count

    return 0


def test(test_file_name: str) -> bool:
    """Test function of this script.

    Args:
        test_file_name (str): full test file processing path

    Returns:
        bool: test successfull
    """
    expected_n_step: int = 6
    n_step: int = main(test_file_name)

    return expected_n_step == n_step


if __name__ == "__main__":
    # file_path: str = join("./Day_8/test.txt")
    file_path: str = join("./Day_8/input.txt")

    print(main(file_path))
