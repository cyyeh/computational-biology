import os


BASE_PATH = f'{os.getcwd()}/rosalind/algorithmic_heights'


def fibonacci_number(n: int) -> int:
    if n <= 1:
        return n

    fibonacci_numbers = [0, 1]
    for _ in range(2, n+1):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers[-1]


def test_fibonacci_number():
    with open(f'{BASE_PATH}/inputs/fib.txt', 'r') as f:
        n = int(f.readline().strip())

    with open(f'{BASE_PATH}/outputs/fib.txt', 'r') as f:
        result = int(f.readline().strip())

    assert fibonacci_number(n) == result
