from functools import lru_cache
import re


def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def p1(filename):
    def evaluate(values, operators):
        result = values[0]
        for i, op in enumerate(operators):
            if op == '+':
                result += values[i + 1]
            elif op == '*':
                result *= values[i + 1]
        return result

    def find_solution(target, values, operators, depth=0):
        if depth == len(operators):
            val = evaluate(values, operators)
            if val == target:
                # print("Solution Found:", *[val for pair in zip(values, operators + ['']) for val in pair])
                return True
            return False

        for op in ['+', '*']:
            new_operators = operators[:]
            new_operators[depth] = op
            if find_solution(target, values, new_operators, depth + 1):
                return True
        return False

    total = 0
    for line in read_gen(filename):
        # print(line)
        r = re.match(r'(\d+): ((?:\d+ ?)+)', line)
        target, values = int(r[1]), list(map(int, r[2].split()))

        # print(target, values)

        operators = ['*'] * (len(values)-1)
        if find_solution(target, values, operators):
            total += target
    
    return total
        


def p2(filename):
    def evaluate(values, operators):
        result = values[0]
        for i, op in enumerate(operators):
            if op == '+':
                result += values[i + 1]
            elif op == '*':
                result *= values[i + 1]
            elif op == '||':
                result = int(str(result) + str(values[i + 1]))
        return result

    def find_solution(target, values, operators, depth=0):
        if depth == len(operators):
            val = evaluate(values, operators)
            if val == target:
                # print("Solution Found:", *[val for pair in zip(values, operators + ['']) for val in pair])
                return True
            return False

        for op in ['+', '*', '||']:
            new_operators = operators[:]
            new_operators[depth] = op
            if find_solution(target, values, new_operators, depth + 1):
                return True
        return False

    total = 0
    for line in read_gen(filename):
        # print(line)
        r = re.match(r'(\d+): ((?:\d+ ?)+)', line)
        target, values = int(r[1]), list(map(int, r[2].split()))

        # print(target, values)

        operators = ['*'] * (len(values)-1)
        if find_solution(target, values, operators):
            total += target
    
    return total



def p1_2(filename):
    def evaluate(target, values):
        n = len(values)

        @lru_cache(None)
        def validate(start, end):
            if start == end:
                return {values[start]}
            
            results = set()
            for i in range(start, end):
                left_results = validate(start, i)
                right_results = validate(i + 1, end)
                for left in left_results:
                    for right in right_results:
                        results.add(left + right)
                        results.add(left * right)
            return results

        all_results = validate(0, n - 1)
        return target in all_results

    total = 0
    for line in read_gen(filename):
        match = re.match(r'(\d+): ((?:\d+ ?)+)', line)
        target, values = int(match[1]), list(map(int, match[2].split()))
        if evaluate(target, values):
            total += target

    print(total)
    return total

def p2_2(filename):
    def can_reach_target(target, values):
        n = len(values)

        # Recursive function to check if target can be reached
        def dfs(start, current_value):
            if start == n:
                return current_value == target
            
            for i in range(start, n):
                # Test addition
                if dfs(i + 1, current_value + values[i]):
                    return True
                
                # Test multiplication
                if dfs(i + 1, current_value * values[i]):
                    return True
                
                # Test concatenation
                concatenated_value = int(str(current_value) + str(values[i]))
                if dfs(i + 1, concatenated_value):
                    return True

            return False

        # Start DFS from the first value
        return dfs(1, values[0])

    total = 0
    for line in read_gen(filename):
        match = re.match(r'(\d+): ((?:\d+ ?)+)', line)
        target, values = int(match[1]), list(map(int, match[2].split()))
        if can_reach_target(target, values):
            total += target

    print(total)
    return total

filename = '2024/7/input.txt'

# print(p1(filename))
# print(p2(filename))
# print(p1_2(filename))
# print(p2_2(filename))

from pybencher import Suite

s = Suite()

s.add(p1, filename)
s.add(p2, filename)
# s.add(p1_2, filename)
# s.add(p2_2, filename)

s.run()