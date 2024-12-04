lines = open('./inputs/day4.txt','r').readlines()
lines = [line.strip() for line in lines]

numbers = list(map(int, lines[0].split(",")))

boards = []
board = []
for line in lines[2:]:
    if board and not line:
        boards.append(board)
        board = []
    elif line:
        board.append(list(map(int, line.split())))

# ============================================================================
def check_board_win(board, called_numbers):
    return any(all(item in called_numbers for item in row) for row in board) or any(all(item in called_numbers for item in col) for col in zip(*board))

def part1(boards, numbers):
    called_numbers = []
    for number in numbers:
        called_numbers.append(number)
        for board in boards:
            if check_board_win(board, called_numbers):
                return number * sum([item for row in board for item in row if item not in called_numbers])

def part2(boards, numbers):
    called_numbers = []
    for number in numbers:
        called_numbers.append(number)
        for board in boards:
            if check_board_win(board, called_numbers):
                if len(boards) == 1:
                    return number * sum([item for row in board for item in row if item not in called_numbers])
                else:
                    boards.remove(board)

print(part1(boards, numbers))
print(part2(boards, numbers))