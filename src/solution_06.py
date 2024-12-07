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
    # Read the input map
    lines = utils.read_lines(input)
    map = [list(line) for line in lines]
    
    # Find the guard's initial position and direction
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    guard_pos = None
    guard_dir = None
    
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell in directions:
                guard_pos = (i, j)
                guard_dir = cell
                break
        if guard_pos:
            break
    
    visited_positions = set()
    visited_positions.add(guard_pos)
    
    while True:
        next_pos = (guard_pos[0] + directions[guard_dir][0], guard_pos[1] + directions[guard_dir][1])
        
        if not (0 <= next_pos[0] < len(map) and 0 <= next_pos[1] < len(map[0])):
            break
        
        if map[next_pos[0]][next_pos[1]] == '#':
            guard_dir = turns[guard_dir]
        else:
            guard_pos = next_pos
            visited_positions.add(guard_pos)
    
    output = len(visited_positions)
    return output

def problem2(input: str) -> int:
    # Read the input map
    lines = utils.read_lines(input)
    map = [list(line) for line in lines]
    
    # Find the guard's initial position and direction
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    guard_pos = None
    guard_dir = None
    
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell in directions:
                guard_pos = (i, j)
                guard_dir = cell
                break
        if guard_pos:
            break
    
    def simulate_guard(map, guard_pos, guard_dir):
        visited_positions = set()
        current_pos = guard_pos
        current_dir = guard_dir
        
        while True:
            next_pos = (current_pos[0] + directions[current_dir][0], current_pos[1] + directions[current_dir][1])
            
            if not (0 <= next_pos[0] < len(map) and 0 <= next_pos[1] < len(map[0])):
                break
            
            if map[next_pos[0]][next_pos[1]] == '#':
                current_dir = turns[current_dir]
            else:
                current_pos = next_pos
                if current_pos in visited_positions:
                    return True
                visited_positions.add(current_pos)
        
        return False
    
    possible_positions = 0
    
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '.' and (i, j) != guard_pos:
                map[i][j] = '#'
                if simulate_guard(map, guard_pos, guard_dir):
                    possible_positions += 1
                map[i][j] = '.'
    
    return possible_positions

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 6)
    print(problem1(input_path))
    print(problem2(input_path))