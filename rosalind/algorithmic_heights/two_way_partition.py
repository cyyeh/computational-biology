import os
from typing import List, Tuple


BASE_PATH = f'{os.getcwd()}/rosalind/algorithmic_heights'


def two_way_partition(nums: List[int]) -> Tuple[List[int], int]:
    if not nums:
        return nums

    # this problem sets the first number as the pivot
    pivot = nums[0]

    # pointer for greater element
    i = len(nums)

    # traverse through all elements
    # compare each element with pivot
    for j in range(len(nums) - 1, 0, -1):
        if nums[j] > pivot:
            # if element bigger than pivot is found
            # swap it with the greater element pointed by i
            i -= 1

            # swapping element at i with element at j
            nums[i], nums[j] = nums[j], nums[i]

    # swap the pivot element with the greater element specified by i
    nums[i - 1], nums[0] = nums[0], nums[i - 1]
    return nums, i - 1


def test_two_way_partition():
    with open(f'{BASE_PATH}/inputs/par.txt', 'r') as f:
        n = int(f.readline().strip())
        numbers = list(map(int, f.readline().strip().split(' ')))

    partitioned, i = two_way_partition(numbers[:n])
    assert all(num <= partitioned[i] for num in partitioned[:i])
    assert all(num > partitioned[i] for num in partitioned[i+1:])


with open(f'{BASE_PATH}/rosalind_par.txt', 'r') as f:
    n = int(f.readline().strip())
    numbers = list(map(int, f.readline().strip().split(' ')))

partitioned, i = two_way_partition(numbers[:n])
print(' '.join(map(str, partitioned)))
