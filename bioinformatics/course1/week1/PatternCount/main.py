import os


BASE_PATH = f'{os.getcwd()}/bioinformatics_algos/course1/week1/PatternCount'


def pattern_count(text: str, pattern: str) -> int:
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count


def test_pattern_count():
    for i in range(1, 9):
        with open(f'{BASE_PATH}/inputs/input_{i}.txt', 'r') as f:
            text, pattern = f.read().splitlines()

        with open(f'{BASE_PATH}/outputs/output_{i}.txt', 'r') as f:
            count = int(f.readline().strip())

        assert pattern_count(text, pattern) == count
