from collections import defaultdict
import os
from typing import List


BASE_PATH = f'{os.getcwd()}/rosalind/algorithmic_heights'


def degree_array(nodes: int, edge_list_data: List[str]) -> List[int]:
    results = [set() for _ in range(nodes)]
    for line in edge_list_data:
        from_node, to_node = map(int, line.split(' '))
        results[from_node - 1].add(to_node - 1)
        results[to_node - 1].add(from_node - 1)
    return list(map(len, results))


def test_degree_array():
    with open(f'{BASE_PATH}/inputs/deg.txt', 'r') as f:
        nodes, _ = map(int, f.readline().strip().split(' ')) # nodes, edges
        edge_list_data = f.read().splitlines()

    with open(f'{BASE_PATH}/outputs/deg.txt', 'r') as f:
        result = f.readline().strip()

    assert ' '.join(map(str, degree_array(nodes, edge_list_data))) == result
