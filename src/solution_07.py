import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import AOC_Helpers as utils
import re
import itertools
import collections
import math

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == '+':
            result += numbers[i]
        elif operators[i-1] == '*':
            result *= numbers[i]
        elif operators[i-1] == '||':
            result = int(str(result) + str(numbers[i]))
    return result

def problem1(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    
    for line in lines:
        test_value, numbers = line.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.strip().split()))
        
        # Generate all possible combinations of operators
        operators = ['+', '*']
        possible = False
        
        for ops in itertools.product(operators, repeat=len(numbers)-1):
            if evaluate_expression(numbers, ops) == test_value:
                possible = True
                break
        
        if possible:
            output += test_value
    
    return output

def problem2(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    
    for line in lines:
        test_value, numbers = line.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.strip().split()))
        
        # Generate all possible combinations of operators including concatenation
        operators = ['+', '*', '||']
        possible = False
        
        for ops in itertools.product(operators, repeat=len(numbers)-1):
            if evaluate_expression(numbers, ops) == test_value:
                possible = True
                break
        
        if possible:
            output += test_value
    
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 7)
    print(problem1(input_path))
    print(problem2(input_path))