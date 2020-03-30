import tkinter
from tkinter.ttk import *

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

import GameOfLife

matplotlib.use("TKAgg")


def game_setup():
    grid_x = int(entr1.get())
    grid_y = int(entr2.get())
    selected_pattern = comboBox.current()
    init_state = [[0 for x in range(0, grid_x)] for y in range(0, grid_y)]
    if selected_pattern == 0: #glider
        init_state[2][2] = 1
        init_state[3][3] = 1
        init_state[4][3] = 1
        init_state[4][2] = 1
        init_state[4][1] = 1

    if selected_pattern == 1: #oscillator
        init_state[3][4] = 1
        init_state[2][4] = 1
        init_state[1][4] = 1

    if selected_pattern == 2: #still life
        init_state[1][4] = 1
        init_state[1][5] = 1
        init_state[3][4] = 1
        init_state[3][5] = 1
        init_state[2][3] = 1
        init_state[2][6] = 1

    if selected_pattern == 3: #random
        init_state = [[np.random.randint(2) for x in range(0, grid_x)] for y in range(0, grid_y)]

    gol = GameOfLife.GameOfLife(grid_x, grid_y, init_state)
    gol.game_of_life()


window = tkinter.Tk()
window.title("The Game of Life")
# window.resizable(0, 0)

label1 = tkinter.Label(window, text=" Grid size x ").grid(row=1, column=2)
entr1 = Entry(window, width=5)
entr1.grid(row=1, column=3)
label2 = tkinter.Label(window, text=" Grid size y ").grid(row=1, column=4)
entr2 = Entry(window, width=5)
entr2.grid(row=1, column=5)
label3 = tkinter.Label(window, text=" Initial state").grid(row=1, column=6)
comboBox = Combobox(window, values=["Glider", "Oscillator", "Still life", "Random"], state="readonly")
comboBox.grid(row=1, column=7)
comboBox.current(0)
bt = tkinter.Button(window, text=" Start game ", command=game_setup)
bt.grid(row=1, column=8)

window.geometry('600x100')

window.mainloop()
#todo try to add interactive state change, custom cell definition, more than one structure in one plot