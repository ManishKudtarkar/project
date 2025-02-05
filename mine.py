import random

# Constants
GRID_SIZE = 5  # Size of the grid (5x5)
NUM_MINES = 5  # Number of mines

# Function to create the grid
def create_grid(size, mines):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    mine_positions = set()
    
    # Place mines randomly
    while len(mine_positions) < mines:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        mine_positions.add((x, y))
    
    for x, y in mine_positions:
        grid[x][y] = 'M'
    
    return grid, mine_positions

# Function to display the grid to the player
def display_grid(grid, revealed):
    print("   " + " ".join([str(i) for i in range(len(grid))]))
    print("  +" + "---+" * len(grid))
    for i, row in enumerate(grid):
        row_display = []
        for j, cell in enumerate(row):
            if revealed[i][j]:
                row_display.append(cell)
            else:
                row_display.append(' ')
        print(f"{i} | {' | '.join(row_display)} |")
        print("  +" + "---+" * len(grid))

# Function to count adjacent mines
def count_adjacent_mines(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[nx][ny] == 'M':
            count += 1
    return count

# Main game function
def play_minesweeper():
    grid, mine_positions = create_grid(GRID_SIZE, NUM_MINES)
    revealed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    safe_cells = GRID_SIZE * GRID_SIZE - NUM_MINES
    
    while True:
        display_grid(grid, revealed)
        try:
            x, y = map(int, input("Enter row and column to reveal (e.g., 1 2): ").split())
            if (x, y) in mine_positions:
                print("Boom! You hit a mine. Game over!")
                break
            if revealed[x][y]:
                print("Cell already revealed. Choose another.")
                continue
            revealed[x][y] = True
            adjacent_mines = count_adjacent_mines(grid, x, y)
            grid[x][y] = str(adjacent_mines) if adjacent_mines > 0 else ' '
            safe_cells -= 1
            if safe_cells == 0:
                print("Congratulations! You cleared the minefield!")
                break
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column numbers.")
    display_grid(grid, [[True] * GRID_SIZE for _ in range(GRID_SIZE)])  # Reveal the entire grid at the end

# Run the game
if __name__ == "__main__":
    play_minesweeper()
