import random

# Constants
BOARD_SIZE = 8
NUM_SHIPS = 3
SHIP_LENGTHS = [3, 4, 5]  # Lengths of ships

# Initialize the game board
board = [["O" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Place ships on the board randomly
def place_ships(board, ship_lengths):
    for length in ship_lengths:
        placed = False
        while not placed:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                ship_row = random.randint(0, BOARD_SIZE - 1)
                ship_col = random.randint(0, BOARD_SIZE - length)
                if all(board[ship_row][ship_col + i] == "O" for i in range(length)):
                    for i in range(length):
                        board[ship_row][ship_col + i] = "S"  # Place ship ('S') horizontally
                    placed = True
            else:  # orientation == 'vertical'
                ship_row = random.randint(0, BOARD_SIZE - length)
                ship_col = random.randint(0, BOARD_SIZE - 1)
                if all(board[ship_row + i][ship_col] == "O" for i in range(length)):
                    for i in range(length):
                        board[ship_row + i][ship_col] = "S"  # Place ship ('S') vertically
                    placed = True

# Function to print the game board
def print_board(board):
    print("\n   1 2 3 4 5 6 7 8")  # Column numbers
    print("  -----------------")
    for i in range(BOARD_SIZE):
        print(f"{i+1}| {' '.join(board[i])} |")  # Row numbers and board contents
    print("  -----------------")

# Function to check if the game is over
def is_game_over(board):
    return all(all(cell != "S" for cell in row) for row in board)

# Main game loop
def play_battleship():
    print("Welcome to Battleship!")
    print("Try to sink all the ships ('S') by guessing their locations.")
    print("Legend:")
    print("  'O' - Empty space")
    print("  'S' - Ship")
    print("  'H' - Hit (you've guessed correctly)")
    print("  'X' - Miss (you've guessed incorrectly)")

    place_ships(board, SHIP_LENGTHS)
    turns = 0

    while True:
        print(f"\nTurn {turns + 1}")
        print_board(board)

        try:
            guess_row = int(input("Guess Row (1-8): ")) - 1
            guess_col = int(input("Guess Column (1-8): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if (guess_row < 0 or guess_row >= BOARD_SIZE) or (guess_col < 0 or guess_col >= BOARD_SIZE):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "H":
            print("You guessed that one already.")
        elif board[guess_row][guess_col] == "S":
            print("You hit a ship!")
            board[guess_row][guess_col] = "H"  # Mark as hit ('H')
            if is_game_over(board):
                print_board(board)
                print("Congratulations! You sank all the battleships!")
                break
        else:
            print("You missed.")
            board[guess_row][guess_col] = "X"  # Mark as missed ('X')

        turns += 1
        if turns >= 20:  # Limiting the number of turns
            print("Game Over. You've reached the maximum number of turns.")
            print("The remaining ships were located as follows:")
            print_board(board)
            break

# Play the game
play_battleship()
