import PySimpleGUI as sg


def create_maze():
    layout = [[sg.Text('Number of rows:'), sg.Input(key='-ROWS-')],
              [sg.Text('Number of columns:'), sg.Input(key='-COLS-')],
              [sg.Button('Submit')]]

    window = sg.Window('Maze Setup', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Submit':
            break

    window.close()

    m = int(values['-ROWS-'])
    n = int(values['-COLS-'])

    layout = [[sg.Button('', size=(2, 1), key=(i,j), pad=(0, 0), button_color=('white', 'white')) for j in range(n)] for i in range(m)]
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
            grid = []
            tmp = "+" * (n + 2)
            grid.append(tmp)
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
                grid.append(row)
            grid.append(tmp)

            if start_existed == 0:
                layout1 = [[sg.Text('Start point not set!')],
                           [sg.Button('OK')]
                           ]
                window1 = sg.Window('Warning',layout1)
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

            with open('grid.txt', 'w') as f:
                for line in grid:
                    f.write(line + "\n")
                window.close()

# create_maze()


def selectAlgorithm():
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