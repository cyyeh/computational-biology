import os
from typing import List


BASE_PATH = f'{os.getcwd()}/rosalind/algorithmic_heights'


def three_way_partition(nums: List[int]) -> List[int]:
    if not nums:
        return nums

    partitioned_val = nums[0]
    start = 0
    end = len(nums) - 1
    i = 0

    while i <= end:
        if nums[i] < partitioned_val:
            nums[i], nums[start] = nums[start], nums[i]
            i += 1
            start += 1
        elif nums[i] > partitioned_val:
            nums[i], nums[end] = nums[end], nums[i]
            end -= 1
        else:
            i += 1

    return nums


def test_three_way_partition():
    with open(f'{BASE_PATH}/inputs/par3.txt', 'r') as f:
        n = int(f.readline().strip())
        numbers = list(map(int, f.readline().strip().split(' ')))

    partitioned = three_way_partition(numbers[:n])
