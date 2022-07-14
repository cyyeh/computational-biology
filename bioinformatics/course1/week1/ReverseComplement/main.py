import os


BASE_PATH = f'{os.getcwd()}/bioinformatics_algos/course1/week1/ReverseComplement'


def reverse_complement(text: str) -> str:
    complement_text = complement(text)
    reversed_complement_text = reverse(complement_text)
    return reversed_complement_text


def complement(text: str) -> str:
    from io import StringIO

    complement_text = StringIO()
    for char in text:
        if char == 'A':
            complement_text.write('T')
        elif char == 'T':
            complement_text.write('A')
        elif char == 'C':
            complement_text.write('G')
        else:
            complement_text.write('C')
    return complement_text.getvalue()

def reverse(text: str) -> str:
    return text[::-1]


def test_reverse_complement():
    for i in range(1, 4):
        with open(f'{BASE_PATH}/inputs/input_{i}.txt', 'r') as f:
            text = f.readline().strip()

        with open(f'{BASE_PATH}/outputs/output_{i}.txt', 'r') as f:
            answer = f.readline().strip()

        assert reverse_complement(text) == answer
