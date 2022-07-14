import os
from typing import List


BASE_PATH = f'{os.getcwd()}/rosalind/algorithmic_heights'


def double_degree_array(nodes: int, edge_list_data: List[str]) -> List[int]:
    adjacency_list = [[] for _ in range(nodes)]
    for line in edge_list_data:
        from_node, to_node = map(int, line.split(' '))
        adjacency_list[from_node - 1].append(to_node - 1)
        adjacency_list[to_node - 1].append(from_node - 1)

    return [
        sum([len(adjacency_list[neighbor]) for neighbor in neighbors])
        for neighbors in adjacency_list
    ]


def test_double_degree_array():
    with open(f'{BASE_PATH}/inputs/ddeg.txt', 'r') as f:
        nodes, edges = map(int, f.readline().strip().split(' '))
        edge_list_data = f.read().splitlines()[:edges]

    with open(f'{BASE_PATH}/outputs/ddeg.txt', 'r') as f:
        result = f.readline().strip()

    assert ' '.join(map(str, double_degree_array(nodes, edge_list_data))) == result
