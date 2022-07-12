'''
Chapter 3: Discovering a Self-Replicating Automaton with Top-Down Programming
'''
from typing import List, NewType


Board = NewType('Board', List[List[bool]])

def play_game_of_life(initial_board: Board, num_generation: int) -> List[Board]:
    boards = [
        initial_board if i == 0 else []
        for i in range(num_generation + 1)
    ]
    for i in range(num_generation):
        boards[i + 1] = update_board(boards[i])
    return boards


def update_board(board: Board) -> Board:
    num_rows = len(board)
    num_cols = len(board[0])
    new_board = initialize_board(num_rows, num_cols)
    for row in range(num_rows):
        for col in range(num_cols):
            new_board[row][col] = update_cell(board, row, col)
    return new_board


def initialize_board(rows: int, cols: int) -> Board:
    return [[False for _ in range(cols)] for _ in range(rows)]


def update_cell(board: Board, row: int, col: int) -> bool:
    num_neighbors = count_live_neighbors(board, row, col)
    if board[row][col]:
        if num_neighbors == 2 or num_neighbors == 3:
            return True
        return False
    else:
        if num_neighbors == 3:
            return True
        return False


def count_live_neighbors(board: Board, row: int, col: int) -> bool:
    live_neighbors = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if (i != row or j != col) and inside_board(board, i, j) and board[i][j]:
                live_neighbors += 1
    return live_neighbors


def inside_board(board: Board, row: int, col: int) -> bool:
    num_rows = len(board)
    num_cols = len(board[0])
    if row < 0 or row > num_rows - 1 or col < 0 or col > num_cols - 1:
        return False
    return True


def print_boards(boards: List[Board]) -> None:
    def print_board(board: Board) -> None:
        for row in board:
            print_row(row)
        print()

    def print_row(row: List[bool]) -> None:
        for cell in row:
            print_cell(cell)
        print()

    def print_cell(val: bool) -> None:
        if val:
            print('⬛', end='')
        else:
            print('⬜', end='')

    for board in boards:
        print_board(board)


if __name__ == '__main__':
    board: Board = [
        [False, False, False, False, False, False],
        [False, True, False, False, False, False],
        [False, False, True, True, True, False],
        [False, True, True, True, False, False],
        [False, False, False, False, True, False],
        [False, False, False, False, False, False],
    ] 
    boards = play_game_of_life(board, 10)
    print_boards(boards)
    '''
    ⬜⬜⬜⬜⬜⬜
    ⬜⬛⬜⬜⬜⬜
    ⬜⬜⬛⬛⬛⬜
    ⬜⬛⬛⬛⬜⬜
    ⬜⬜⬜⬜⬛⬜
    ⬜⬜⬜⬜⬜⬜

    ⬜⬜⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬜⬜⬛⬜
    ⬜⬛⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬜⬜⬜⬜

    ⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬛⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜

    ⬜⬜⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬜⬜⬛⬜
    ⬜⬛⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬜⬜⬜⬜

    ⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬛⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜

    ⬜⬜⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬜⬜⬛⬜
    ⬜⬛⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬜⬜⬜⬜

    ⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬛⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜

    ⬜⬜⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬜⬜⬛⬜
    ⬜⬛⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬜⬜⬜⬜

    ⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬛⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜

    ⬜⬜⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬜⬜⬛⬜
    ⬜⬛⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬜⬜⬜⬜

    ⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬜⬛⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜
    '''