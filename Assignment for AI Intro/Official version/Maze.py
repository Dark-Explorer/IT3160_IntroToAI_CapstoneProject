import turtle
import time
import sys
from collections import deque

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Solving Program")
wn.setup(1300, 700)


class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0.5)


# Path found by algorithm(s)
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0.5)


class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0.5)


# Agent class
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0.5)


class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0.5)


grid = [
"+++++++++++++++",
"+s+       + +e+",
"+ +++++ +++ + +",
"+ + +       + +",
"+ +   +++ + + +",
"+ + + +   + + +",
"+   + +   + + +",
"+++++ +   + + +",
"+     +   +   +",
"+++++++++++++++",
]

# grid = [
# "+++++++++",
# "+ ++s++++",
# "+ ++ ++++",
# "+ ++ ++++",
# "+    ++++",
# "++++ ++++",
# "++++ ++++",
# "+      e+",
# "+++++++++",
# ]

# grid = [
# "+++++++++++++++",
# "+             +",
# "+             +",
# "+             +",
# "+     e       +",
# "+             +",
# "+             +",
# "+             +",
# "+ s           +",
# "+++++++++++++++",
# ]
# grid = [
#     "+++++++++++++++++++++++++++++++++++++++++++++++++++",
#     "+               +                                 +",
#     "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
#     "+s          +                 +               ++  +",
#     "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
#     "+  +     +  +           +  +                 +++  +",
#     "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
#     "+  +  +  +  +  +  +        +  +  +        +       +",
#     "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
#     "+  +     +  +          +   +           +  +  ++  ++",
#     "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
#     "+     +  +     +              +              ++   +",
#     "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
#     "+  +  +                    +     +     +  +  +++  +",
#     "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
#     "+  +  +     +     +     +  +  +     +     +  ++  ++",
#     "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
#     "+                       +  +  +              ++  ++",
#     "+ ++++++             +  +  +  +  +++        +++  ++",
#     "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
#     "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
#     "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
#     "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
#     "+      ++ +++++++e+++     ++          ++    +++++++",
#     "+++++++++++++++++++++++++++++++++++++++++++++++++++",
# ]


# grid = [
#     "+++++++++++++++++++++",
#     "++++++    +++++++++++",
#     "++++++   ++++++++++++",
#     "++++++  +++++++++ e +",
#     "++++++ +++++++++++  +",
#     "++++++ ++++++++++++ +",
#     "++++++ +++++++++++  +",
#     "++++++             ++",
#     "+++++++++++++++++  ++",
#     "+++++++++++++++++  ++",
#     "+++++++++++++++++  ++",
#     "++++++++++++++     ++",
#     "s                  ++",
#     "+++++++++++++++++++++",
# ]

def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == " " or character == "e":
                path.append((screen_x, screen_y))

            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)
                end_x, end_y = screen_x, screen_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()


def bfs(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    while len(frontier) > 0:
        time.sleep(0.9)
        x, y = frontier.popleft()

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
            #print(solution)

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
            print(solution)

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

def backRoute(x, y):
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

walls = []
path = []
visited = set()
frontier = deque()
solution = {}

# Main program
setup_maze(grid)
bfs(start_x, start_y)
backRoute(end_x, end_y)
wn.exitonclick()
