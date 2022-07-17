import os
from typing import List, Set


BASE_PATH = f'{os.getcwd()}/rosalind/algorithmic_heights'


class DFSStack:
    def __init__(self, nodes: int):
        self._stack = []
        self._visited = set()
        self._not_visited = {node for node in range(nodes)}

    def push(self, data: List[int]) -> None:
        for node in data:
            if node not in self._visited:
                self._stack.append(node)
                self._visited.add(node)
                self._not_visited.remove(node)

    def pop(self) -> int:
        return self._stack.pop()

    def empty(self) -> bool:
        return not self._stack

    def is_visited(self, node: int) -> bool:
        return node in self._visited

    @property
    def visited(self) -> Set[int]:
        return self._visited

    @property
    def not_visited(self) -> Set[int]:
        return self._not_visited


def connected_components(nodes: int, edge_list_data: List[str]) -> int:
    adjacency_list = [[] for _ in range(nodes)]
    for line in edge_list_data:
        from_node, to_node = map(int, line.split(' '))
        adjacency_list[from_node - 1].append(to_node - 1)
        adjacency_list[to_node - 1].append(from_node - 1)

    num_connected_components = 0
    s = DFSStack(nodes)
    for node in range(nodes):
        if not s.is_visited(node):
            s.push([node])
            num_connected_components += 1
            while not s.empty():
                last_node = s.pop()
                s.push(adjacency_list[last_node])

    return num_connected_components


def test_connected_components():
    with open(f'{BASE_PATH}/inputs/cc.txt', 'r') as f:
        nodes, edges = map(int, f.readline().strip().split(' ')) # nodes, edges
        edge_list_data = f.read().splitlines()[:edges]

    with open(f'{BASE_PATH}/outputs/cc.txt', 'r') as f:
        result = int(f.readline().strip())

    assert connected_components(nodes, edge_list_data) == result
