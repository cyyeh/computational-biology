import os


BASE_PATH = f'{os.getcwd()}/bioinformatics_algos/course1/week2/HammingDistance'


def hamming_distance(str1: str, str2) -> int:
    result = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            result += 1
    return result


def test_hamming_distance():
    for i in range(1, 9):
        with open(f'{BASE_PATH}/inputs/input_{i}.txt', 'r') as f:
            str1 = f.readline().strip()
            str2 = f.readline().strip()

        with open(f'{BASE_PATH}/outputs/output_{i}.txt', 'r') as f:
            result = int(f.readline().strip())

        assert hamming_distance(str1, str2) == result
