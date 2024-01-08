import random

def generate_maze(width, height):
    maze = [['+'] * (width + 2)]
    for i in range(height):
        row = ['+']
        for j in range(width):
            if random.random() < 0.7:
                row.append('+')
            else:
                row.append(' ')
        row.append('+')
        maze.append(row)
    maze.append(['+'] * (width + 2))
    maze[1][1] = 's'
    maze[-2][-2] = 'e'

    visited = set()
    stack = [(1, 1)]
    while stack:
        (x, y) = stack.pop()
        if (x, y) == (width - 1, height - 2):
            break
        if (x, y) in visited:
            continue
        visited.add((x, y))

        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        random.shuffle(neighbors)
        for (nx, ny) in neighbors:
            if maze[ny][nx] == ' ':
                stack.append((nx, ny))
                maze[ny][nx] = '+'

    return maze

width, height = 20, 10
maze = generate_maze(width, height)
for row in maze:
    print(''.join(str(cell) for cell in row))
