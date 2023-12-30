import random

def generate_maze(width, height):
    # Increase the maze dimensions to account for borders
    width_with_border = width + 2
    height_with_border = height + 2

    # Initialize the maze grid with walls
    maze = [['+' for _ in range(width_with_border)] for _ in range(height_with_border)]

    # Set the starting position
    start_x = random.randint(1, width)
    start_y = random.randint(1, height)
    maze[start_y][start_x] = ' '

    # Generate the maze using depth-first search with larger moves
    stack = [(start_x, start_y)]
    while stack:
        x, y = stack.pop()

        directions = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
        random.shuffle(directions)

        for dx, dy in directions:
            if dx >= 1 and dx < width_with_border - 1 and dy >= 1 and dy < height_with_border - 1 and maze[dy][dx] == '+':
                maze[y + (dy - y) // 2][x + (dx - x) // 2] = ' '
                maze[dy][dx] = ' '
                stack.append((dx, dy))

    # Set the goal position
    goal_x = random.randint(1, width)
    goal_y = random.randint(1, height)
    maze[goal_y][goal_x] = 'e'

    goal_x = random.randint(1, width)
    goal_y = random.randint(1, height)
    maze[goal_y][goal_x] = 's'

    # Convert the maze grid to a string representation
    maze_str = '\n'.join(''.join(row) for row in maze)

    return maze_str


# Example usage
width = 50
height = 30
maze = generate_maze(width, height)
print(maze)
with open("34.txt", 'w') as file:
    file.write(maze)