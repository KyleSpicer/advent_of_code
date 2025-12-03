# AoC 2024, day 15

from copy import deepcopy as dc

SAMPLE_FILE = "sample.txt"
DATA_FILE = "data.txt"

dirs = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}


def print_gameboard(game_board):
    for row in game_board:
        print(row)


def get_start_pos(game_board) -> tuple:
    for i, row in enumerate(game_board):
        for j, col in enumerate(row):
            if "@" == game_board[i][j]:
                return (i, j)


def process_move(game_board, direction):
    start_x, start_y = get_start_pos(game_board)
    dir_x, dir_y = dirs[direction]
    next_x, next_y = start_x, start_y

    print(start_x, start_y)


def part_one(board, directions):
    print(directions)
    print("Initial State:")
    print_gameboard(board)

    for curr_dir in directions:
        print(f"\nMove {curr_dir}: ")
        print_gameboard(board)
        process_move(board, curr_dir)
        break


def main():
    with open(SAMPLE_FILE, "r") as file:
        game_board, directions = file.read().split("\n\n")

    game_board = [list(x) for x in game_board.split("\n")]
    directions = list(directions)

    part_one_answer = part_one(dc(game_board), directions)
    print(f"{part_one_answer = }")


if __name__ == "__main__":
    main()
