from .run import part_1, part_2
from src.utils import read_input_lines

input_sample_0 = read_input_lines('src/2023/day_template/input_sample_0.txt')
input_sample_1 = read_input_lines('src/2023/day_template/input_sample_1.txt')
input_sample_2 = read_input_lines('src/2023/day_template/input_sample_2.txt')
input = read_input_lines('src/2023/day_template/input.txt')


def test_part_1():
    assert part_1(input) == 0


def test_part_2():
    assert part_2(input) == 0
