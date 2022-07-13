import os
from typing import List


BASE_PATH = f'{os.getcwd()}/bioinformatics_algos/course1/week2/ApproximatePatternMatching'


def hamming_distance(str1: str, str2) -> int:
    result = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            result += 1
    return result


def approximate_pattern_matching(text: str, pattern: str, mismatches: int) -> List[int]:
    results = []
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i:i+len(pattern)], pattern) <= mismatches:
            results.append(i)
    return results


def test_approximate_pattern_matching():
    for i in range(1, 9):
        with open(f'{BASE_PATH}/inputs/input_{i}.txt', 'r') as f:
            text = f.readline().strip()
            pattern = f.readline().strip()
            mismatches = int(f.readline().strip())

        with open(f'{BASE_PATH}/outputs/output_{i}.txt', 'r') as f:
            result = f.readline().strip()

        assert ' '.join(map(str, approximate_pattern_matching(text, pattern, mismatches))) == result
