import os
from typing import List


BASE_PATH = f'{os.getcwd()}/rosalind/algorithmic_heights'


def insertion_sort(numbers: List[int]) -> int:
    if len(numbers) < 2:
        return 0

    swaps = 0
    for i, _ in enumerate(numbers[1:]):
        k = i + 1
        while k > 0 and numbers[k] < numbers[k-1]:
            numbers[k], numbers[k-1] = numbers[k-1], numbers[k]
            swaps += 1
            k -= 1
    return swaps


def test_insertion_sort():
    with open(f'{BASE_PATH}/inputs/ins.txt', 'r') as f:
        n = int(f.readline().strip())
        numbers = list(map(int, f.readline().strip().split(' ')))

    with open(f'{BASE_PATH}/outputs/ins.txt', 'r') as f:
        result = int(f.readline().strip())

    assert insertion_sort(numbers[:n]) == result
