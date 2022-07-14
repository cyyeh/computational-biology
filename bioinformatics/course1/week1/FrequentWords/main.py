from collections import defaultdict
import os
from typing import DefaultDict, Dict, List


BASE_PATH = f'{os.getcwd()}/bioinformatics_algos/course1/week1/FrequentWords'


def frequent_words(text: str, k: int) -> List[str]:
    frequent_patterns = []
    freq_map = frequency_table(text, k)
    max_val = max_map(freq_map)
    for pattern in freq_map:
        if freq_map[pattern] == max_val:
            frequent_patterns.append(pattern)
    return frequent_patterns


def frequency_table(text: str, k: int) -> DefaultDict[str, int]:
    freq_map = defaultdict(int)
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i+k]
        freq_map[pattern] += 1
    return freq_map


def max_map(map: Dict[str, int]) -> int:
    return max(map.values())


def test_pattern_count():
    for i in range(1, 7):
        with open(f'{BASE_PATH}/inputs/input_{i}.txt', 'r') as f:
            text = f.readline().strip()
            k = int(f.readline().strip())

        with open(f'{BASE_PATH}/outputs/output_{i}.txt', 'r') as f:
            patterns = f.readline().strip()

        assert ' '.join(sorted(frequent_words(text, k))) == patterns
