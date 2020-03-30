import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class GameOfLife(object):
    def __init__(self, grid_size_x, grid_size_y, init_state):
        self.init_state = init_state
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.imgs = []

    def get_neighbors(self, row, column):

        if row == 0:
            previous_row = self.grid_size_x - 1
        else:
            previous_row = row - 1
        if row == self.grid_size_x - 1:
            next_row = 0
        else:
            next_row = row + 1
        if column == 0:
            previous_column = self.grid_size_y - 1
        else:
            previous_column = column - 1
        if column == self.grid_size_y - 1:
            next_column = 0
        else:
            next_column = column + 1
        neighbors_list = [self.init_state[previous_row][previous_column], self.init_state[previous_row][column],
                          self.init_state[previous_row][next_column], self.init_state[row][previous_column],
                          self.init_state[row][next_column], self.init_state[next_row][previous_column],
                          self.init_state[next_row][column], self.init_state[next_row][next_column]]

        return neighbors_list

    def count_living_neighbors(self, neighbors_list):
        alive_neighbors_count = 0
        for neighbor in neighbors_list:
            if neighbor == 1:
                alive_neighbors_count += 1
        return alive_neighbors_count

    def calculate_next_state(self):

        next_states = [[0 for i in range(self.grid_size_x)] for j in range(self.grid_size_y)]
        for cell_i, i in enumerate(self.init_state):
            for cell_j, j in enumerate(i):
                neighbors_list = self.get_neighbors(cell_i, cell_j)
                alive_neighbors_count = self.count_living_neighbors(neighbors_list)
                if self.init_state[cell_i][cell_j] == 1:
                    if alive_neighbors_count < 2 or alive_neighbors_count > 3:
                        next_states[cell_i][cell_j] = 0
                    if alive_neighbors_count == 2 or alive_neighbors_count == 3:
                        next_states[cell_i][cell_j] = 1
                else:
                    if alive_neighbors_count == 3:
                        next_states[cell_i][cell_j] = 1
        self.init_state = next_states
        return self.init_state

    def game_of_life(self):
        fig = plt.figure()
        # print(self.init_state)
        plt.imshow(self.init_state, interpolation="nearest")
        for i in range(0, 100):
            next_states = self.calculate_next_state()
            im = plt.imshow(next_states, animated=True)
            self.imgs.append([im])
        ani = animation.ArtistAnimation(fig, self.imgs, interval=500, blit=True)
        plt.show()
