import os
from typing import List


BASE_PATH = f'{os.getcwd()}/bioinformatics_algos/course1/week1/PatternMatching'


def pattern_matching(pattern: str, text: str) -> List[int]:
    results = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            results.append(i)
    return results


def test_pattern_matching():
    for i in range(1, 7):
        with open(f'{BASE_PATH}/inputs/input_{i}.txt', 'r') as f:
            pattern = f.readline().strip()
            genome = f.readline().strip()

        with open(f'{BASE_PATH}/outputs/output_{i}.txt', 'r') as f:
            results = f.readline().strip()

        assert ' '.join(map(str, pattern_matching(pattern, genome))) == results
