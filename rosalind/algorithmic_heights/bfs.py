import os
from queue import Queue
from typing import List, Tuple


BASE_PATH = f'{os.getcwd()}/rosalind/algorithmic_heights'


class BFSQueue:
    def __init__(self):
        self._q = Queue()

    def get(self) -> Tuple[int, int]:
        return self._q.get()

    def put(self, data: List[int], depth: int) -> None:
        for node in data:
            self._q.put((node, depth))

    def empty(self) -> bool:
        return self._q.empty()


def bfs(nodes: int, edge_list_data: List[str]) -> List[int]:
    adjacency_list = [[] for _ in range(nodes)]
    for line in edge_list_data:
        from_node, to_node = map(int, line.split(' '))
        adjacency_list[from_node - 1].append(to_node - 1)

    results = [0] + [-1] * (nodes - 1)
    q = BFSQueue()
    if adjacency_list[0]:
        q.put(adjacency_list[0], 1)
    while not q.empty():
        node, depth = q.get()
        results[node] = depth
        if adjacency_list[node]:
            q.put(adjacency_list[node], depth + 1)

    return results

def test_bfs():
    with open(f'{BASE_PATH}/inputs/bfs.txt', 'r') as f:
        nodes, _ = map(int, f.readline().strip().split(' ')) # nodes, edges
        edge_list_data = f.read().splitlines()

    with open(f'{BASE_PATH}/outputs/bfs.txt', 'r') as f:
        result = f.readline().strip()

    assert ' '.join(map(str, bfs(nodes, edge_list_data))) == result
