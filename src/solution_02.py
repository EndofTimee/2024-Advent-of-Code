import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import AOC_Helpers as utils
import re
import itertools
import collections
import math


def is_safe_report(levels):
    increasing = all(1 <= levels[i+1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(1 <= levels[i] - levels[i+1] <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing

def is_safe_report_with_dampener(levels):
    if is_safe_report(levels):
        return True
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe_report(new_levels):
            return True
    return False

def problem1(input: str) -> int:
    lines = utils.read_lines(input)
    safe_count = 0
    
    for line in lines:
        levels = list(map(int, line.split()))
        if is_safe_report(levels):
            safe_count += 1
    
    return safe_count

def problem2(input: str) -> int:
    lines = utils.read_lines(input)
    safe_count = 0
    
    for line in lines:
        levels = list(map(int, line.split()))
        if is_safe_report_with_dampener(levels):
            safe_count += 1
    
    return safe_count

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 2)
    print(problem1(input_path))
    print(problem2(input_path))