import random
import os

def generate_maze(width, height):
    # Increase the maze dimensions to account for borders
    width_with_border = width + 2
    height_with_border = height + 2

    # Initialize the maze grid with walls
    maze = [['+' for _ in range(width_with_border)] for _ in range(height_with_border)]

    # Set the starting position
    start_x = random.randint(1, width)
    start_y = random.randint(1, height)
    maze[start_y][start_x] = 's'

    # Generate the maze using depth-first search
    stack = [(start_x, start_y)]
    while stack:
        x, y = stack[-1]
        maze[y][x] = ' '

        directions = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
        random.shuffle(directions)

        path_available = False
        for dx, dy in directions:
            if dx >= 1 and dx < width_with_border - 1 and dy >= 1 and dy < height_with_border - 1 and maze[dy][dx] == '+':
                maze[y + (dy - y) // 2][x + (dx - x) // 2] = ' '
                maze[dy][dx] = ' '
                stack.append((dx, dy))
                path_available = True
                break

        if not path_available:
            stack.pop()

    # Set the goal position
    goal_x = random.randint(1, width)
    goal_y = random.randint(1, height)
    maze[goal_y][goal_x] = 'e'

    # Add borders to the maze
    maze_with_border = ['+' * width_with_border]
    for row in maze[1:-1]:
        maze_with_border.append('+' + ''.join(row[1:-1]) + '+')
    maze_with_border.append('+' * width_with_border)

    # Convert the maze grid to a string representation
    maze_str = '\n'.join(maze_with_border)

    # Ensure there is a path from start to goal
    maze_str = maze_str.replace('s', ' ')
    maze_str = maze_str.replace('e', ' ')
    maze_str = maze_str[:start_y * (width_with_border + 1) + start_x] + 's' + maze_str[start_y * (width_with_border + 1) + start_x + 1:]
    maze_str = maze_str[:goal_y * (width_with_border + 1) + goal_x] + 'e' + maze_str[goal_y * (width_with_border + 1) + goal_x + 1:]

    return maze_str

for i in range (1, 91):
    filename = f'maze_{i}'
    folderpath = os.path.join(os.getcwd(), 'Assignment for AI Intro/Official version/MazeForStatistics')
    filepath = os.path.join(folderpath, filename)
    with open(filepath, 'w') as file:
        file.write(generate_maze(50, 30))