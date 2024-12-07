import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import AOC_Helpers as utils
import re
import itertools
import collections
import math

def problem1(input: str) -> int:
    lines = utils.read_lines(input)
    left_list = []
    right_list = []

    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()

    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    return total_distance

def problem2(input: str) -> int:
    lines = utils.read_lines(input)
    left_list = []
    right_list = []

    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    right_count = collections.Counter(right_list)

    similarity_score = sum(num * right_count[num] for num in left_list)

    return similarity_score

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 1)
    print(problem1(input_path))
    print(problem2(input_path))