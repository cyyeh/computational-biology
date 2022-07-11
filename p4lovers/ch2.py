'''
Chapter 2: Forecasting a Presidential Election with Monte Carlo Simulation
'''
import random
from typing import Callable, List, Tuple

from prologue import trivia_gcd, euclid_gcd

random.seed(123)

def weighted_die(rolls: int = 1) -> List[int]:
    return random.choices(
        [1, 2, 3, 4, 5, 6],
        weights=[.1, .1, .5, .1, .1, .1],
        k=rolls
    )


def show_running_time_average_comparison_table(
    func1: Callable = trivia_gcd,
    func2: Callable = euclid_gcd,
    ranges: List[Tuple[int, int]] = [
        (1000, 2000),
        (10000, 20000),
        (100000, 200000),
        (1000000, 2000000)
    ],
    pairs: int = 10
) -> None:
    def generate_randomly_chosen_pairs(
        ranges: List[Tuple[int, int]],
        pairs: int
    ) -> List[List[Tuple[int, int]]]:
        return [
            [
                (
                    random.randint(min_num, max_num),
                    random.randint(min_num, max_num)
                )
                for _ in range(pairs)
            ]
            for (min_num, max_num) in ranges
        ]

    def get_func_running_time(func: Callable, *args) -> float:
        import time

        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()

        return end - start

    def get_func_average_running_times(
        func: Callable,
        ranges: List[List[Tuple[int, int]]]
    ) -> List[float]:
        import statistics

        return [
            statistics.mean([
                get_func_running_time(func, *pair)
                for pair in chosen_pairs
            ])
            for chosen_pairs in ranges
        ]

    def print_running_time_average_comparison_table(
        func1: Callable,
        func2: Callable,
        ranges: List[Tuple[int, int]],
        func1_timing_results: List[float],
        func2_timing_results: List[float]
    ) -> None:
        print(f'{func1.__name__:>52} | {func2.__name__:>25}')
        for i in range(len(ranges)):
            print(
                f'{ranges[i][0]:>10} to {ranges[i][1]:>10} | '
                f'{func1_timing_results[i]:>25} | '
                f'{func2_timing_results[i]:>25}'
            )

    chosen_pairs_in_ranges = generate_randomly_chosen_pairs(ranges, pairs)
    func1_timing_results = get_func_average_running_times(func1, chosen_pairs_in_ranges)
    func2_timing_results = get_func_average_running_times(func2, chosen_pairs_in_ranges)
    print_running_time_average_comparison_table(func1, func2, ranges, func1_timing_results, func2_timing_results)


if __name__ == '__main__':
    show_running_time_average_comparison_table()