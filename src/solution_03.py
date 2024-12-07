import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import AOC_Helpers as utils
import re
import itertools
import collections
import math

def problem1(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    
    for line in lines:
        matches = pattern.findall(line)
        for match in matches:
            x, y = map(int, match)
            output += x * y
    
    return output

def problem2(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")
    
    mul_enabled = True
    
    for line in lines:
        for part in re.split(r'(\bdo\(\)|\bdon\'t\(\))', line):
            if do_pattern.match(part):
                mul_enabled = True
            elif dont_pattern.match(part):
                mul_enabled = False
            else:
                matches = mul_pattern.findall(part)
                for match in matches:
                    if mul_enabled:
                        x, y = map(int, match)
                        output += x * y
    
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 3)
    print(problem1(input_path))
    print(problem2(input_path))