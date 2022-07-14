import os
from typing import List


BASE_PATH = f'{os.getcwd()}/rosalind/algorithmic_heights'


def binary_search(sorted_numbers: List[int], target: int) -> int:
    left_idx = 0
    right_idx = len(sorted_numbers) - 1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if sorted_numbers[mid_idx] == target:
            return mid_idx + 1
        elif sorted_numbers[mid_idx] > target:
            right_idx = mid_idx - 1
        else:
            left_idx = mid_idx + 1
    return -1


def binary_searches(sorted_numbers: List[int], targets: List[int]) -> List[int]:
    return [binary_search(sorted_numbers, num) for num in targets]


def test_binary_searches():
    with open(f'{BASE_PATH}/inputs/bins.txt', 'r') as f:
        n = int(f.readline().strip())
        m = int(f.readline().strip())
        sorted_numbers = list(map(int, f.readline().strip().split(' ')))
        targets = list(map(int, f.readline().strip().split(' ')))

    with open(f'{BASE_PATH}/outputs/bins.txt', 'r') as f:
        result = f.readline().strip()

    assert ' '.join(map(str, binary_searches(sorted_numbers[:n], targets[:m]))) == result
