import random

def generate_maze(width, height):
    random.seed()
    maze = [['+'] * (width + 2)]
    for i in range(height):
        row = ['+']
        for j in range(width):
            if random.random() < 0.3:
                row.append('+')
            else:
                row.append(' ')
        row.append('+')
        maze.append(row)
    maze.append(['+'] * (width + 2))

    maze[1][1] = 's'
    maze[-2][-2] = 'e'
    return maze

# width, height = 50, 30
# maze = generate_maze(width, height)
# mazeStr = ""
# for row in maze:
#     print(''.join(str(cell) for cell in row))
#     mazeStr += ''.join(str(cell) for cell in row)
#     mazeStr += "\n"

for i in range(0, 1):
    filename = str(i) + ".txt"
    width, height = 30, 30
    maze = generate_maze(width, height)
    mazeStr = ""
    for row in maze:
        # print(''.join(str(cell) for cell in row))
        mazeStr += ''.join(str(cell) for cell in row)
        mazeStr += "\n"
    with open(filename, 'w') as file:
        file.write(mazeStr)
