import collections
import itertools
from pathlib import Path
import sys
from typing import Tuple
from math import floor

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import AOC_Helpers as utils
import re
import math

def problem1(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    
    antenna_positions = collections.defaultdict(list)
    
    # Step 1: Read the input and store antenna positions
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char.isalnum():
                antenna_positions[char].append((x, y))
    
    antinodes = set()
    
    # Step 2: Calculate antinodes for each frequency
    for positions in antenna_positions.values():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                
                # Calculate potential antinode positions
                dx = x2 - x1
                dy = y2 - y1
                
                # Antinode positions
                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)
                
                # Check if antinode positions are within bounds
                if 0 <= antinode1[0] < len(lines[0]) and 0 <= antinode1[1] < len(lines):
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < len(lines[0]) and 0 <= antinode2[1] < len(lines):
                    antinodes.add(antinode2)
    
    # Step 3: Count unique antinode positions
    output = len(antinodes)
    
    return output

def problem2(input: str) -> int | str:
    output: int = 0 
    grid = utils.parse_grid(utils.read_file(input))

    sims: dict[str, list[Tuple[int, int]]] = {}

    antinodes = [[0 for _ in i] for i in grid]
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == ".":
                continue
            if grid[y][x] not in sims:
                sims[grid[y][x]] = []
            sims[grid[y][x]].append((x, y))

    def is_in_bounds(x, y, grid):
        if floor(x) != x or floor(y) != y:
            return False
        return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

    for k, v in sims.items():
        for i in range(len(v)):
            for j in range(len(v)):
                if i == j:
                    continue
                dist: Tuple[int, int] = (v[j][0] - v[i][0], v[j][1] - v[i][1])
                for mul in itertools.count(0):
                    wow = (dist[0] * mul, dist[1] * mul)
                    fails = 0
                    if is_in_bounds(v[i][0]-wow[0], v[i][1]-wow[1], grid):
                        antinodes[v[i][1]-wow[1]][v[i][0]-wow[0]] = 1
                    else:
                        fails=1
                    if is_in_bounds(v[j][0]+wow[0], v[j][1]+wow[1], grid):
                        antinodes[v[j][1]+wow[1]][v[j][0]+wow[0]] = 1
                    elif fails:
                        break
    for y in range(len(antinodes)):
        for x in range(len(antinodes[y])):
            if antinodes[y][x] == 1:
                output += 1
                grid[y][x] = "#"
    
    for k in antinodes:
        print("".join([str(i) for i in k]))

    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 8)
    print(problem1(input_path))
    print(problem2(input_path))