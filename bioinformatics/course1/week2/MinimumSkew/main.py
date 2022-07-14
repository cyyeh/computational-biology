import os
from typing import List


BASE_PATH = f'{os.getcwd()}/bioinformatics_algos/course1/week2/MinimumSkew'


def minimum_skew(genome: str) -> List[int]:
    g_c_differences = [0]
    for nucleotide in genome:
        if nucleotide == 'C':
            g_c_differences.append(g_c_differences[-1] - 1)
        elif nucleotide == 'G':
            g_c_differences.append(g_c_differences[-1] + 1)
        else:
            g_c_differences.append(g_c_differences[-1])

    min_skew = min(g_c_differences)
    return [idx for idx, val in enumerate(g_c_differences) if val == min_skew]


def test_minimum_skew():
    for i in range(1, 7):
        with open(f'{BASE_PATH}/inputs/input_{i}.txt', 'r') as f:
            genome = f.readline().strip()

        with open(f'{BASE_PATH}/outputs/output_{i}.txt', 'r') as f:
            result = f.readline().strip()

        assert ' '.join(map(str, minimum_skew(genome))) == result
