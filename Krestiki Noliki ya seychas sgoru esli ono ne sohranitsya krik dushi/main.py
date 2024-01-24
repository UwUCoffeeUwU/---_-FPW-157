print('Крестики-Нолики, игра началась!')


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winnerwinnerchickendinner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Игрок {current_player}, введите номер строки (0, 1, 2): "))
        col = int(input(f"Игрок {current_player}, введите номер столбца (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winnerwinnerchickendinner(board)

            if winner:
                print_board(board)
                print(f"Winner Winner Chicken Dinner! Игрок {winner} победил!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Ничья! Давайте еще партию!?")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Эта ячейка уже занята. Попробуйте снова.")

if __name__ == "__main__":
    main()
