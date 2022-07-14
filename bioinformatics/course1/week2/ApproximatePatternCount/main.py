import os


BASE_PATH = f'{os.getcwd()}/bioinformatics_algos/course1/week2/ApproximatePatternCount'


def hamming_distance(str1: str, str2) -> int:
    result = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            result += 1
    return result


def approximate_pattern_count(text: str, pattern: str, mismatches: int) -> int:
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i:i+len(pattern)], pattern) <= mismatches:
            count += 1
    return count


def test_approximate_pattern_matching():
    for i in range(1, 3):
        with open(f'{BASE_PATH}/inputs/input_{i}.txt', 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
            mismatches = int(f.readline().strip())

        with open(f'{BASE_PATH}/outputs/output_{i}.txt', 'r') as f:
            result = int(f.readline().strip())

        assert approximate_pattern_count(text, pattern, mismatches) == result
