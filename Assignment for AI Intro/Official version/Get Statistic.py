import turtle
import time
import sys
import os
from collections import deque
import PySimpleGUI as sg

global input_grid
global start_x, start_y, end_x, end_y

def unsolvable():
    unreachable = [[sg.Text('No path can be found')]]
    window = sg.Window('Warning', unreachable)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            sys.exit()
        window.close()

def get_name_without_extension(file_path):
    filename, file_extension = os.path.splitext(os.path.basename(file_path))
    return filename

def solve_maze(file_path):
    with open(file_path, 'r') as f:
        input_grid = []
        for line in f:
            row = line.strip()
            input_grid.append(row)
    setup_maze(input_grid)
    maze_name = get_name_without_extension(file_path)
    global walls_count, path_count
    info = (str) (maze_name) + " " + (str) (walls_count) + " " + (str) (path_count) + " "
    aglorithms = [bfs, dfs, aStar]
    for aglorithm in aglorithms:
        with open("statistic.txt", 'a') as file:
            file.write(info)
        aglorithm(start_x, start_y)
        back_route(end_x, end_y)
        reset_variables()

def handle_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            solve_maze(file_path)
    clear_all()


def reset_variables():
    global visited, frontier, solution
    visited = set()
    frontier.clear()
    solution.clear()

def clear_all():
    global walls, path, visited, frontier, solution
    walls = []
    path = []
    visited = set()
    frontier.clear()
    solution.clear()

# Maze by Turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Solving Program")
wn.setup(10, 10)

class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

class Black(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

def update_window_size(grid):
    base_cell_size = 24
    num_rows = len(grid)
    num_cols = len(grid[0])

    window_width = num_cols * base_cell_size
    window_height = num_rows * base_cell_size

    wn.setup(width=window_width + 50, height=window_height + 50)

def setup_maze(grid):
    global walls_count, path_count
    walls_count = 0
    path_count = 0
    update_window_size(grid)
    maze_width = len(grid[0]) * 24
    maze_height = len(grid) * 24

    screen_x_start = -maze_width / 2
    screen_y_start = maze_height / 2

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]

            screen_x = (x * 24) + screen_x_start
            screen_y = screen_y_start - (y * 24)

            maze.goto(screen_x, screen_y)

            if character == "+":
                maze.stamp()
                walls.append((screen_x, screen_y))
                walls_count += 1

            elif character == " ":
                path.append((screen_x, screen_y))
                path_count += 1

            if character == "e":
                path.append((screen_x, screen_y))
                green.color("purple")
                green.goto(screen_x, screen_y)
                green.stamp()
                green.color("green")
                global end_x, end_y
                end_x, end_y = screen_x, screen_y

            if character == "s":
                global start_x, start_y
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)
                red.stamp()
    walls_count = walls_count - 2 * len(grid) - 2 * len(grid[0]) + 4
    path_count += 2
    with open("statistic.txt", 'a') as file:
        file.write("Maze - Walls - Paths - Visited - Solution" + "\n")

def end_program(x, y):
    wn.bye()  
    sys.exit()

def bfs(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    while len(frontier) > 0:
        x, y = frontier.popleft()

        if (end_x, end_y) in visited:
            break
        if (x - 24, y) in path and (x - 24, y) not in visited:
            cell = (x - 24, y)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x - 24, y))

        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell = (x, y - 24)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))

        if (x + 24, y) in path and (x + 24, y) not in visited:
            cell = (x + 24, y)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x + 24, y))

        if (x, y + 24) in path and (x, y + 24) not in visited:
            cell = (x, y + 24)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x, y)
        green.stamp()

    print("Visited: ", len(visited))
    with open("statistic.txt", 'a') as file:
        file.write((str)(" bfs ") + (str)(len(visited)))
    if (end_x, end_y) not in visited:
        unsolvable()

def dfs(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    while len(frontier) > 0:
        x, y = frontier.pop()

        if (end_x, end_y) in visited:
            break
        if (x - 24, y) in path and (x - 24, y) not in visited:
            cell = (x - 24, y)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x - 24, y))

        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell = (x, y - 24)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))

        if (x + 24, y) in path and (x + 24, y) not in visited:
            cell = (x + 24, y)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x + 24, y))

        if (x, y + 24) in path and (x, y + 24) not in visited:
            cell = (x, y + 24)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x, y)
        green.stamp()
    print("Visited: ", len(visited))
    with open("statistic.txt", 'a') as file:
        file.write((str)(" dfs ") + (str)(len(visited)))
    if (end_x, end_y) not in visited:
        unsolvable()

def heuristic(x, y):
    return abs(x - end_x) * abs(x - end_x) + abs(y - end_y) * abs(y - end_y)

def aStar(x, y):
    open_set = set()
    closed_set = set()
    came_from = {}

    g_score = {(x, y): 0}
    h_score = {(x, y): heuristic(x, y)}
    f_score = {(x, y): h_score[(x, y)]}

    solution[x, y] = x, y
    open_set.add((x, y))

    while open_set:
        (a, b) = min(open_set, key=lambda node: f_score[node])

        open_set.remove((a, b))
        closed_set.add((a, b))

        if (a, b) == (end_x, end_y):
            break

        for (next_x, next_y) in [(a + 24, b), (a - 24, b), (a, b + 24), (a, b - 24)]:
            if (next_x, next_y) in path:
                if (next_x, next_y) in closed_set:
                    continue

                tentative_g_score = g_score[(a, b)] + 24

                if (next_x, next_y) not in open_set or tentative_g_score < g_score[(next_x, next_y)]:
                    came_from[(next_x, next_y)] = (a, b)
                    g_score[(next_x, next_y)] = tentative_g_score
                    h_score[(next_x, next_y)] = heuristic(next_x, next_y)
                    f_score[(next_x, next_y)] = g_score[(next_x, next_y)] + h_score[(next_x, next_y)]

                    solution[(next_x, next_y)] = (a, b)

                    if (next_x, next_y) not in open_set:
                        open_set.add((next_x, next_y))
                    blue.goto((next_x, next_y))
                    blue.stamp()

        green.goto(a, b)
        green.stamp()
    print("Visited: ", len(closed_set))
    # print("Length of solution: ", len(solution))
    with open("statistic.txt", 'a') as file:
        file.write((str)(" astar ") + (str)(len(closed_set)))
    if (end_x, end_y) not in solution:
        unsolvable()


def back_route(x, y):
    global solution
    yellow.goto(x, y)
    yellow.stamp()
    len = 1
    while (x, y) != (start_x, start_y):
        len += 1
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]
    print("Length of solution: " + (str)(len))
    with open("statistic.txt", 'a') as file:
        file.write((str)(len) + "\n")

# set up classes
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
black = Black()

# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}

# main program
folderpath = os.path.join(os.getcwd(), 'Assignment for AI Intro/Official version/MazeForStatistics')
handle_folder(folderpath)
wn.onclick(end_program)
turtle.mainloop()