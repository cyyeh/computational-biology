import os
from typing import List


BASE_PATH = f'{os.getcwd()}/rosalind/algorithmic_heights'


def three_sum(nums: List[int]) -> List[int]:
    for i, num in enumerate(nums):
        results = two_sum(nums[i+1:], -num)
        if results != [-1]:
            return [i + 1] + [result + i + 1 for result in results]
    return [-1]


def two_sum(nums: List[int], target: int) -> List[int]:
    num_idx_map = {}
    for i, num in enumerate(nums):
        if target - num in num_idx_map:
            return [num_idx_map[target - num] + 1, i + 1]
        else:
            num_idx_map[num] = i

    return [-1]


def three_sums(arrays_of_nums: List[List[int]]) -> List[List[int]]:
    return [three_sum(nums) for nums in arrays_of_nums]        


def test_three_sums():
    with open(f'{BASE_PATH}/inputs/3sum.txt', 'r') as f:
        array_num, array_size = map(int, f.readline().strip().split(' '))
        arrays_of_nums = [
            list(map(int, line.split(' ')[:array_size]))
            for line in f.read().splitlines()[:array_num]
        ]

    with open(f'{BASE_PATH}/outputs/3sum.txt', 'r') as f:
        results = [
            list(map(int, line.split(' ')))
            for line in f.read().splitlines()
        ]

    assert three_sums(arrays_of_nums) == results
