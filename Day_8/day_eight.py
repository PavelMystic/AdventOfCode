"""Implementation of the Day 8 assignment."""

from os.path import join
from itertools import cycle

START_NODE: str = "A"
END_NODE: str = "Z"
LR_DICT: dict[str, int] = {"L": 0, "R": 1}


def node_to_lr(node: str) -> tuple[str, tuple[str, ...]]:
    node_parts: list[str] = node.split(" = ")
    assert len(node_parts) == 2, "Wrong node format!"

    node_parts[1] = node_parts[1].replace("(", "").replace(")", "")
    lr_part: list[str] = node_parts[1].split(", ")

    return node_parts[0], tuple(lr_part)


def get_specific_noes(node_names: list[str], specific_last_letter: str) -> list[str]:
    return [name for name in node_names if list(name)[-1] == specific_last_letter]


def main(main_file_name: str) -> int:
    """Main processing function of this script.

    Args:
        main_file_name (str): full main file path

    Returns:
        int: number of steps required to get from AAA to ZZZ
    """

    node_map: dict[str, tuple[str, ...]] = {}

    with open(main_file_name, "r", encoding="utf-8") as file:
        for line_idx, line in enumerate(file):
            if line_idx == 0:
                instructions: str = line.strip()
            if line_idx >= 2:
                node_name, lr_part = node_to_lr(line.strip())
                node_map[node_name] = lr_part

    current_node_names: list[str] = get_specific_noes(node_map.keys(), START_NODE)
    end_node_names: list[str] = get_specific_noes(node_map.keys(), END_NODE)
    step_count: int = 0

    for instruction in cycle(instructions):
        for curent_idx, current_node in enumerate(current_node_names):
            current_node_names[curent_idx] = node_map[current_node][
                LR_DICT[instruction]
            ]
        step_count += 1

        if step_count % 1000000 == 1:
            print(f"=============== Step {step_count} ===============")
            print(f"{current_node_names}")
            print(f"{end_node_names}")

        if all([current_node in end_node_names for current_node in current_node_names]):
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
