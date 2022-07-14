import os
from typing import List


BASE_PATH = f'{os.getcwd()}/rosalind/algorithmic_heights'


def majority_element(nums: List[int]) -> int:
    from collections import Counter

    c = Counter(nums)
    most_common = c.most_common(1)[0]
    num, count = most_common
    if count <= len(nums) // 2:
        return -1

    return num


def majority_elements(arrays_of_nums: List[List[int]]) -> List[int]:
    return [majority_element(nums) for nums in arrays_of_nums]        


def test_majority_elements():
    with open(f'{BASE_PATH}/inputs/maj.txt', 'r') as f:
        array_num, array_size = map(int, f.readline().strip().split(' '))
        arrays_of_nums = [
            list(map(int, line.split(' ')[:array_size]))
            for line in f.read().splitlines()[:array_num]
        ]

    with open(f'{BASE_PATH}/outputs/maj.txt', 'r') as f:
        results = f.readline().strip()

    assert ' '.join(map(str, majority_elements(arrays_of_nums))) == results
