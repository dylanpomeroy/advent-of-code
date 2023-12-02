from .run import part_1, part_2
from src.utils import read_input_lines

input = read_input_lines('src/2023/day_1/input.txt')


def test_part_1():
    assert part_1([]) == 0


def test_part_2():
    assert part_2(input) == 54277
