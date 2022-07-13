from collections import defaultdict
import os
from typing import DefaultDict, Set, Tuple


BASE_PATH = f'{os.getcwd()}/bioinformatics_algos/course1/week1/ClumpFinding'


def clump_finding(
    text: str,
    pattern_length: int,
    window_length: int,
    min_showing_times: int
) -> Set[str]:
    patterns = set()
    text_length = len(text)
    freq_map = defaultdict(int)
    for i in range(text_length - window_length + 1):
        if i == 0:
            freq_map, patterns = init_frequency_table_and_patterns(
                text[i:i+window_length],
                pattern_length,
                freq_map,
                patterns,
                min_showing_times
            )
        else:
            freq_map, patterns = update_frequency_table_and_patterns(
                text,
                i,
                window_length,
                pattern_length,
                freq_map,
                patterns,
                min_showing_times
            )

    return patterns


def init_frequency_table_and_patterns(
    text: str,
    pattern_length: int, 
    freq_map: DefaultDict[str, int],
    patterns: Set[str],
    min_showing_times: int
) -> Tuple[DefaultDict[str, int], Set[str]]:
    text_length = len(text)
    for i in range(text_length - pattern_length + 1):
        pattern = text[i:i+pattern_length]
        freq_map[pattern] += 1
        if freq_map[pattern] >= min_showing_times:
            patterns.add(pattern)
    return freq_map, patterns


def update_frequency_table_and_patterns(
    text: str,
    index: int,
    window_length: int,
    pattern_length: int,
    freq_map: DefaultDict[str, int],
    patterns: Set[str],
    min_showing_times: int
) -> Tuple[DefaultDict[str, int], Set[str]]:
    window = text[index:index+window_length]
    last_window = text[index-1:index-1+window_length]
    first_pattern_in_last_window = last_window[:pattern_length]
    freq_map[first_pattern_in_last_window] -= 1            
    last_pattern_in_window = window[-pattern_length:]
    freq_map[last_pattern_in_window] += 1

    if freq_map[last_pattern_in_window] >= min_showing_times:
        patterns.add(last_pattern_in_window)

    return freq_map, patterns


def test_clump_finding():
    for i in range(1, 6):
        with open(f'{BASE_PATH}/inputs/input_{i}.txt', 'r') as f:
            pattern = f.readline().strip()
            pattern_length, window_length, min_showing_times = map(int, f.readline().strip().split(' '))

        with open(f'{BASE_PATH}/outputs/output_{i}.txt', 'r') as f:
            result = f.readline().strip()

        assert clump_finding(pattern, pattern_length, window_length, min_showing_times) == set(result.split(' '))


if __name__ == '__main__':
    with open(f'{BASE_PATH}/E_coli.txt', 'r') as f:
        pattern = f.readline().strip()

    print(len(clump_finding(pattern, 9, 500, 3)))