import os
from typing import List


BASE_PATH = f'{os.getcwd()}/rosalind/algorithmic_heights'


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    sorted1 = merge_sort(nums[:mid])
    sorted2 =  merge_sort(nums[mid:])
    return merge_two_sorted(sorted1, sorted2)


def merge_two_sorted(sorted1: List[int], sorted2: List[int]) -> List[int]:
    merged = []
    sorted1_idx = 0
    sorted2_idx = 0

    while sorted1_idx < len(sorted1) and sorted2_idx < len(sorted2):
        if sorted1[sorted1_idx] <= sorted2[sorted2_idx]:
            merged.append(sorted1[sorted1_idx])
            sorted1_idx += 1
        else:
            merged.append(sorted2[sorted2_idx])
            sorted2_idx += 1

    if sorted1_idx == len(sorted1):
        merged += sorted2[sorted2_idx:]
    else:
        merged += sorted1[sorted1_idx:]

    return merged


def test_merge_sort():
    with open(f'{BASE_PATH}/inputs/ms.txt', 'r') as f:
        n = int(f.readline().strip())
        numbers = list(map(int, f.readline().strip().split(' ')))

    with open(f'{BASE_PATH}/outputs/ms.txt', 'r') as f:
        results = f.readline().strip()

    assert ' '.join(map(str, merge_sort(numbers[:n]))) == results
