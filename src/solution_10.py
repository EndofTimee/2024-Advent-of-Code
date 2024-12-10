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
    
    # Parse the topographic map
    map_height = len(lines)
    map_width = len(lines[0])
    topographic_map = [[int(height) for height in line] for line in lines]
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def bfs(start):
        queue = collections.deque([start])
        visited = set([start])
        reachable_nines = 0
        
        while queue:
            x, y = queue.popleft()
            current_height = topographic_map[x][y]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < map_height and 0 <= ny < map_width and (nx, ny) not in visited:
                    next_height = topographic_map[nx][ny]
                    if next_height == current_height + 1:
                        if next_height == 9:
                            reachable_nines += 1
                        queue.append((nx, ny))
                        visited.add((nx, ny))
        
        return reachable_nines
    
    # Find all trailheads and calculate their scores
    for i in range(map_height):
        for j in range(map_width):
            if topographic_map[i][j] == 0:
                output += bfs((i, j))
    
    return output

def problem2(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    
    # Parse the topographic map
    map_height = len(lines)
    map_width = len(lines[0])
    topographic_map = [[int(height) for height in line] for line in lines]
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(x, y, visited):
        if topographic_map[x][y] == 9:
            return 1
        
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < map_height and 0 <= ny < map_width and (nx, ny) not in visited:
                if topographic_map[nx][ny] == topographic_map[x][y] + 1:
                    visited.add((nx, ny))
                    count += dfs(nx, ny, visited)
                    visited.remove((nx, ny))
        
        return count
    
    # Find all trailheads and calculate their ratings
    for i in range(map_height):
        for j in range(map_width):
            if topographic_map[i][j] == 0:
                visited = set([(i, j)])
                output += dfs(i, j, visited)
    
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 10)
    print(problem1(input_path))
    print(problem2(input_path))