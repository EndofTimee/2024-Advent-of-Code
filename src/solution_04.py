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
    
    word = "XMAS"
    word_len = len(word)
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1),  # right, down, down-right, down-left
        (0, -1), (-1, 0), (-1, -1), (-1, 1)  # left, up, up-left, up-right
    ]
    
    def is_valid(x, y):
        return 0 <= x < len(lines) and 0 <= y < len(lines[0])
    
    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or lines[nx][ny] != word[i]:
                return False
        return True
    
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            for dx, dy in directions:
                if search_from(i, j, dx, dy):
                    output += 1
    
    return output

def problem2(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    
    pattern = [
        [(0, 0), (1, -1), (1, 1), (2, -2), (2, 2)],  # MAS in X shape
        [(0, 0), (1, 1), (1, -1), (2, 2), (2, -2)],  # MAS in X shape (mirrored)
    ]
    
    def is_valid(x, y):
        return 0 <= x < len(lines) and 0 <= y < len(lines[0])
    
    def search_pattern(x, y, pattern):
        for dx, dy in pattern:
            nx, ny = x + dx, y + dy
            if not is_valid(nx, ny):
                return False
            if (dx, dy) in [(0, 0), (2, -2), (2, 2)] and lines[nx][ny] != 'M':
                return False
            if (dx, dy) in [(1, -1), (1, 1)] and lines[nx][ny] != 'A':
                return False
        return True
    
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            for pat in pattern:
                if search_pattern(i, j, pat):
                    output += 1
    
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 4)
    print(problem1(input_path))
    print(problem2(input_path))