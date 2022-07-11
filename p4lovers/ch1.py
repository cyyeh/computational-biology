'''
We now have two biological problems to solve as the central goals of this chapter.

1. Given a shorter ori within a longer genome, what is the hidden message indicating
    that replication should start in this region?
2. Given a bacterial genome, where is ori?
'''
from collections import defaultdict
from typing import Dict, List


def pattern_count(text: str, pattern: str) -> int:
    '''
    Substring Counting Problem

    Input: A string pattern and a longer string text.

    Output: The number of times that pattern occurs as a substring of text.

    >>> pattern_count("CGATATATCCATAG", "ATA")
    3
    '''
    import re
    return len(re.findall(f'(?={pattern})', text))


def frequent_words(text: str, k: int) -> List[str]:
    '''
    Frequent Words Problem

    Input: A string text and an integer k.

    Output: All most frequent k-mers(a string of length k) in text.
    >>> frequent_words('atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagatag' + \
        'gtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttg' + \
        'tgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgt' + \
        'tttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacat' + \
        'gcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatc' + \
        'atgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc', 9)
    ['atgatcaag', 'ctcttgatc', 'tcttgatca', 'cttgatcat']
    '''
    def frequency_table(text: str, k: int) -> Dict[str, int]:
        freq_map = defaultdict(int)
        n = len(text)
        for i in range(n - k):
            pattern = text[i:i + k]
            freq_map[pattern] += 1
        return freq_map

    def max_map(map: Dict[str, int]) -> int:
        return max(map.values())

    frequent_patterns = []
    freq_map = frequency_table(text, k)
    max_value = max_map(freq_map)
    for pattern in freq_map:
        if freq_map[pattern] == max_value:
            frequent_patterns.append(pattern)
    return frequent_patterns


def reverse_complement(pattern: str) -> str:
    '''
    Reverse Complement Problem

    Input: A DNA string pattern.

    Output: The reverse complement of pattern.
    
    >>> reverse_complement('agtcgcatagt')
    'actatgcgact'
    '''
    def complement(pattern: str) -> str:
        from io import StringIO
        
        complement_pattern = StringIO()
        
        for ch in pattern:
            if ch == 'a':
                complement_pattern.write('t')
            elif ch == 't':
                complement_pattern.write('a')
            elif ch == 'c':
                complement_pattern.write('g')
            else:
                complement_pattern.write('c')
        
        return complement_pattern.getvalue()

    def reverse(pattern: str) -> str:
        return pattern[::-1]

    return reverse(complement(pattern))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
