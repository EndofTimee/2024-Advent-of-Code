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
    
    # Separate rules and updates
    rules = []
    updates = []
    is_update_section = False
    
    for line in lines:
        if line.strip() == "":
            is_update_section = True
            continue
        if is_update_section:
            updates.append(list(map(int, line.split(','))))
        else:
            rules.append(tuple(map(int, line.split('|'))))
    
    def is_correctly_ordered(update, rules):
        index_map = {page: idx for idx, page in enumerate(update)}
        for x, y in rules:
            if x in index_map and y in index_map and index_map[x] > index_map[y]:
                return False
        return True
    
    middle_pages = []
    
    for update in updates:
        if is_correctly_ordered(update, rules):
            middle_index = len(update) // 2
            middle_pages.append(update[middle_index])
    
    output = sum(middle_pages)
    return output

def problem2(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    
    # Separate rules and updates
    rules = []
    updates = []
    is_update_section = False
    
    for line in lines:
        if line.strip() == "":
            is_update_section = True
            continue
        if is_update_section:
            updates.append(list(map(int, line.split(','))))
        else:
            rules.append(tuple(map(int, line.split('|'))))
    
    def is_correctly_ordered(update, rules):
        index_map = {page: idx for idx, page in enumerate(update)}
        for x, y in rules:
            if x in index_map and y in index_map and index_map[x] > index_map[y]:
                return False
        return True
    
    def topological_sort(update, rules):
        graph = {page: [] for page in update}
        in_degree = {page: 0 for page in update}
        
        for x, y in rules:
            if x in graph and y in graph:
                graph[x].append(y)
                in_degree[y] += 1
        
        queue = collections.deque([page for page in update if in_degree[page] == 0])
        sorted_update = []
        
        while queue:
            node = queue.popleft()
            sorted_update.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return sorted_update
    
    middle_pages = []
    
    for update in updates:
        if not is_correctly_ordered(update, rules):
            sorted_update = topological_sort(update, rules)
            middle_index = len(sorted_update) // 2
            middle_pages.append(sorted_update[middle_index])
    
    output = sum(middle_pages)
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 5)
    print(problem1(input_path))
    print(problem2(input_path))