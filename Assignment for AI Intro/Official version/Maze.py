import turtle
import time
import sys
from collections import deque
import PySimpleGUI as sg

global input_grid


# Set up the maze with PySimpleGUI
def method_setup():
    layout = [[sg.Text('Select how you want to create maze: ')],
              [sg.Button('Import File'), sg.Button('Use GUI')]
              ]
    window = sg.Window('Welcome', layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Use GUI':
            window.close()
            create_maze_with_GUI()
        elif event == 'Import File':
            import_layout = [[sg.Text('Choose file to import:')],
                             [sg.Input(), sg.FileBrowse()],
                             [sg.OK()]
                             ]
            window1 = sg.Window('Import File', import_layout)
            event1, values1 = window1.read()
            if event1 == 'OK':
                global input_grid
                filename = values1[0]
                with open(filename, 'r') as f:
                    input_grid = []
                    for line in f:
                        row = line.strip()
                        input_grid.append(row)
            window1.close()
            window.close()


def create_maze_with_GUI():
    layout = [[sg.Text('Number of rows:'), sg.Input(size=(5, 1), key='-ROWS-')],
              [sg.Text('Number of columns:'), sg.Input(size=(5, 1), key='-COLS-')],
              [sg.Button('Submit')]]

    window = sg.Window('Maze Setup', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Submit':
            break

    window.close()

    m = int(values['-ROWS-'])
    n = int(values['-COLS-'])

    layout = [[sg.Button('', size=(2, 1), key=(i, j), pad=(0, 0), button_color=('white', 'white')) for j in range(n)] for i in range(m)]
    layout.append([sg.Button('Set Start'), sg.Button('Set End'), sg.Button('Set Wall')])
    layout.append([sg.Button('Submit')])

    window = sg.Window('Maze Setup', layout)

    start_set = False
    end_set = False
    wall_set = True
    start = end = None

    start_existed = 0
    end_existed = 0

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if type(event) == tuple:
            button = window[event]
            if wall_set:
                if button.ButtonColor[1] == 'white':
                    button.update(button_color=('white', 'black'))
                elif button.ButtonColor[1] == 'black':
                    button.update(button_color=('white', 'white'))
            elif start_set:
                if start:
                    start.update(button_color=('white', 'white'))
                button.update(button_color=('white', 'red'))
                start = button
            elif end_set:
                if end:
                    end.update(button_color=('white', 'white'))
                button.update(button_color=('white', 'purple'))
                end = button
        elif event == 'Set Start':
            start_set = True
            end_set = False
            wall_set = False
        elif event == 'Set End':
            end_set = True
            start_set = False
            wall_set = False
        elif event == 'Set Wall':
            wall_set = True
            start_set = False
            end_set = False
        elif event == 'Submit':
            global input_grid
            input_grid = []
            tmp = "+" * (n + 2)
            input_grid.append(tmp)
            for i in range(m):
                row = '+'
                for j in range(n):
                    button = window[(i, j)]
                    if button.ButtonColor[1] == 'black':
                        row += '+'
                    elif button.ButtonColor[1] == 'white':
                        row += ' '
                    elif button.ButtonColor[1] == 'red':
                        row += 's'
                        start_existed = 1
                    elif button.ButtonColor[1] == 'purple':
                        row += 'e'
                        end_existed = 1
                row += '+'
                input_grid.append(row)
            input_grid.append(tmp)

            if start_existed == 0:
                layout1 = [[sg.Text('Start point not set!')],
                            [sg.Button('OK')]
                            ]
                window1 = sg.Window('Warning', layout1)
                event1, values1 = window1.read()
                if event1 == 'OK':
                    window1.close()

            if end_existed == 0:
                layout1 = [[sg.Text('End point not set!')],
                            [sg.Button('OK')]
                            ]
                window1 = sg.Window('Warning', layout1)
                event1, values1 = window1.read()
                if event1 == 'OK':
                    window1.close()
            if start_existed == 1 and end_existed == 1:
                break

    window.close()


def select_algorithm():
    layout = [[sg.Text('Choose the algorithm you want to solve this maze with:')],
              [sg.Button('BFS'), sg.Button('DFS'), sg.Button('A*')]
              ]

    window = sg.Window('Select Algorithm', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'BFS':
            window.close()
            bfs(start_x, start_y)
        elif event == 'DFS':
            window.close()
            dfs(start_x, start_y)
        elif event == 'A*':
            window.close()
            print('A* still developing')


# Maze by Turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Solving Program")
wn.setup(1300, 700)

global start_x, start_y, end_x, end_y


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


# this is the class for the yellow or turtle
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


# with open('grid.txt', 'r') as f:
#     grid = []
#     for line in f:
#         row = line.strip()
#         grid.append(row)


def setup_maze(grid):  # define a function called setup_maze
    # global start_x, start_y, end_x, end_y  # set up global variables for start and end locations
    for y in range(len(grid)):  # read in the grid line by line
        for x in range(len(grid[y])):  # read each cell in the line
            character = grid[y][x]  # assign the variable "character" the x and y location on the grid
            screen_x = -588 + (x * 24)  # move to the x location on the screen staring at -588
            screen_y = 288 - (y * 24)  # move to the y location of the screen starting at 288

            if character == "+":
                maze.goto(screen_x, screen_y)  # move pen to the x and y location and
                maze.stamp()  # stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))  # add coordinate to walls list

            if character == " " or character == "e":
                path.append((screen_x, screen_y))  # add " " and e to path list

            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)  # send green sprite to screen location
                global end_x, end_y, start_x, start_y
                end_x, end_y = screen_x, screen_y  # assign end locations variables to end_x and end_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)


def end_program():
    wn.exitonclick()
    sys.exit()


def bfs(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    while len(frontier) > 0:  # exit while loop when frontier queue equals zero
        time.sleep(0.1)
        x, y = frontier.popleft()  # pop next entry in the frontier queue an assign to x and y location

        if (x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            solution[cell] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(cell)  # identify frontier cells
            blue.stamp()
            frontier.append(cell)  # add cell to frontier list
            visited.add((x - 24, y))  # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            # print(solution)

        if (x + 24, y) in path and (x + 24, y) not in visited:  # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x + 24, y))

        if (x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x, y)
        green.stamp()


def dfs(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    while len(frontier) > 0:
        time.sleep(0.1)
        x, y = frontier.pop()
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
            # print(solution)

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


def back_route(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]


# set up classes
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}

# main program starts here
method_setup()
setup_maze(input_grid)
select_algorithm()
back_route(end_x, end_y)
end_program()
