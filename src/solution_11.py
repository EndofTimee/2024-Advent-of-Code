import sys
import os
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import AOC_Helpers as utils

def transform_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        half_len = len(str(stone)) // 2
        left_half = int(str(stone)[:half_len])
        right_half = int(str(stone)[half_len:])
        return [left_half, right_half]
    else:
        return [stone * 2024]

def count_stones_after_blinks(initial_stones, num_blinks):
    stone_counts = defaultdict(int)
    for stone in initial_stones:
        stone_counts[stone] += 1
    
    for _ in range(num_blinks):
        new_stone_counts = defaultdict(int)
        for stone, count in stone_counts.items():
            transformed_stones = transform_stone(stone)
            for new_stone in transformed_stones:
                new_stone_counts[new_stone] += count
        stone_counts = new_stone_counts
    
    return sum(stone_counts.values())

def problem1(input: str) -> int | str:
    stones = list(map(int, utils.read_lines(input)[0].split()))
    return count_stones_after_blinks(stones, 25)

def problem2(input: str) -> int | str:
    stones = list(map(int, utils.read_lines(input)[0].split()))
    return count_stones_after_blinks(stones, 75)

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 11)
    print(problem1(input_path))
    print(problem2(input_path))