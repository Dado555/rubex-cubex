import random
import numpy as np
from rubicks_visualize_console import *
import copy

moves = ["U", "L", "F", "R", "B", "D",
         "U'", "D'", "F'", "B'", "R'", "L'"]

colours_dict = {
    'w': white_center_sq,
    'o': orange_center_sq,
    'r': red_center_sq,
    'g': green_center_sq,
    'b': blue_center_sq,
    'y': yellow_center_sq
}


def convert_array_to_color(array):
    if array[0] == 1:
        return 'o'
    elif array[1] == 1:
        return 'g'
    elif array[2] == 1:
        return 'r'
    elif array[3] == 1:
        return 'b'
    elif array[4] == 1:
        return 'w'
    else:
        return 'y'


def gen_random_moves(moves_num):
    return [random.choice(moves) for i in range(moves_num)]


def scramble_cube():
    # random 25 do 30 poteza za mjesanje kocke
    # moves_num = random.randint(25, 30)
    moves_num = 25
    gen_moves = [random.choice(moves) for i in range(moves_num)]
    return scramble(gen_moves), gen_moves


finish_state = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
                ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'], [
    'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']]


class Cube:
    def __init__(self):
        self.state = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
                      ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'], [
                          'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
                      ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']]

    def get_state(self):
        return self.state

    def get_state_copy(self):
        return copy.deepcopy(self.get_state())

    def set_state(self, new_state):
        self.state = new_state

    # def __init__(self, cube):
    #     self.state = copy.deepcopy(cube.get_state())

    def face_move(self, x):
        self.state[x][0], self.state[x][6], self.state[x][4], self.state[x][2] = self.state[x][6], self.state[x][4], \
            self.state[x][2], self.state[x][0]
        self.state[x][1], self.state[x][7], self.state[x][5], self.state[x][3] = self.state[x][7], self.state[x][5], \
            self.state[x][3], self.state[x][1]
        return

    def face_move_prime(self, x):
        self.state[x][0], self.state[x][2], self.state[x][4], self.state[x][6] = self.state[x][2], self.state[x][4], \
            self.state[x][6], self.state[x][0]
        self.state[x][1], self.state[x][3], self.state[x][5], self.state[x][7] = self.state[x][3], self.state[x][5], \
            self.state[x][7], self.state[x][1]
        return

    def swap(self, x1, x2, x3, x4, y1, y2, y3, y4):
        self.state[x1][y1], self.state[x2][y2], self.state[x3][y3], self.state[x4][y4] = self.state[x2][y2], \
            self.state[x3][
            y3], self.state[x4][y4], \
            self.state[x1][y1]

    def print_cube(self):
        print(
            "    " + self.state[0][0] + self.state[0][1] + self.state[0][2] + "\n" +
            "    " + self.state[0][3] + "w" + self.state[0][4] + "\n" +
            "    " + self.state[0][5] + self.state[0][6] + self.state[0][7] + "\n\n" +

            self.state[1][0] + self.state[1][1] + self.state[1][2] + " " + self.state[2][0] + self.state[2][1] +
            self.state[2][2] + " " + self.state[3][0] + self.state[3][1] + self.state[3][2] + " " + self.state[4][0] +
            self.state[4][1] + self.state[4][2] + "\n" +

            self.state[1][3] + "o" + self.state[1][4] + " " + self.state[2][3] + "g" + self.state[2][4] + " " +
            self.state[3][3] + "r" + self.state[3][4] + " " + self.state[4][3] + "b" + self.state[4][4] + "\n" +

            self.state[1][5] + self.state[1][6] + self.state[1][7] + " " + self.state[2][5] + self.state[2][6] +
            self.state[2][7] + " " + self.state[3][5] + self.state[3][6] + self.state[3][7] + " " + self.state[4][5] +
            self.state[4][6] + self.state[4][7] + "\n\n" +

            "    " + self.state[5][0] + self.state[5][1] + self.state[5][2] + "\n" +
            "    " + self.state[5][3] + "y" + self.state[5][4] + "\n" +
            "    " + self.state[5][5] +
            self.state[5][6] + self.state[5][7] + "\n"
        )

    def check_if_final(self):
        for i in range(0, 6):
            for j in range(0, 8):
                if self.state[i][j] != finish_state[i][j]:
                    return False
        return True

    def convert_from_np_array(self, np_array):
        iter = 0
        for side in range(0, len(np_array)):
            state_row = 0
            if iter == 0:
                state_row = 1
            elif iter == 8:
                state_row = 2
            elif iter == 16:
                state_row = 3
            elif iter == 24:
                state_row = 4
            elif iter == 32:
                state_row = 0
            else:
                state_row = 5

            sqr_color = convert_array_to_color(np_array[side])
            self.state[state_row][side % 8] = sqr_color

            if side % 8 == 7:
                iter += 8

    def convert_to_np_array(self):
        return np.concatenate([np.array([colours_dict[i] for i in self.state[1]]),
                               np.array([colours_dict[i]
                                         for i in self.state[2]]),
                               np.array([colours_dict[i]
                                         for i in self.state[3]]),
                               np.array([colours_dict[i]
                                         for i in self.state[4]]),
                               np.array([colours_dict[i]
                                         for i in self.state[0]]),
                               np.array([colours_dict[i] for i in self.state[5]])], axis=0)

    def convert_to_array_for_nn(self):
        array1 = np.concatenate([colours_dict[i] for i in self.state[1]])
        array2 = np.concatenate([colours_dict[i] for i in self.state[2]])
        array3 = np.concatenate([colours_dict[i] for i in self.state[3]])
        array4 = np.concatenate([colours_dict[i] for i in self.state[4]])
        array5 = np.concatenate([colours_dict[i] for i in self.state[0]])
        array6 = np.concatenate([colours_dict[i] for i in self.state[5]])
        ret = np.concatenate(
            [array1, array2, array3, array4, array5, array6], axis=0)
        return np.expand_dims(ret, axis=0)


def rotate_cube(state, rotation_letter, move_index):
    if rotation_letter == 'U':
        state.face_move(move_index)
        state.swap(1, 2, 3, 4, 0, 0, 0, 0)
        state.swap(1, 2, 3, 4, 1, 1, 1, 1)
        state.swap(1, 2, 3, 4, 2, 2, 2, 2)
    elif rotation_letter == "U'":
        state.face_move_prime(move_index)
        state.swap(1, 4, 3, 2, 0, 0, 0, 0)
        state.swap(1, 4, 3, 2, 1, 1, 1, 1)
        state.swap(1, 4, 3, 2, 2, 2, 2, 2)
    elif rotation_letter == 'U2':
        rotate_cube(state, 'U', move_index)
        rotate_cube(state, 'U', move_index)
    elif rotation_letter == 'D':
        state.face_move(move_index)
        state.swap(1, 4, 3, 2, 4, 4, 4, 4)
        state.swap(1, 4, 3, 2, 5, 5, 5, 5)
        state.swap(1, 4, 3, 2, 6, 6, 6, 6)
    elif rotation_letter == "D'":
        state.face_move_prime(move_index)
        state.swap(1, 2, 3, 4, 4, 4, 4, 4)
        state.swap(1, 2, 3, 4, 5, 5, 5, 5)
        state.swap(1, 2, 3, 4, 6, 6, 6, 6)
    elif rotation_letter == 'D2':
        rotate_cube(state, 'D', move_index)
        rotate_cube(state, 'D', move_index)
    elif rotation_letter == 'R':
        state.face_move(move_index)
        state.swap(0, 2, 5, 4, 2, 2, 2, 6)
        state.swap(0, 2, 5, 4, 3, 3, 3, 7)
        state.swap(0, 2, 5, 4, 4, 4, 4, 0)
    elif rotation_letter == "R'":
        state.face_move_prime(move_index)
        state.swap(0, 4, 5, 2, 2, 6, 2, 2)
        state.swap(0, 4, 5, 2, 3, 7, 3, 3)
        state.swap(0, 4, 5, 2, 4, 0, 4, 4)
    elif rotation_letter == 'R2':
        rotate_cube(state, 'R', move_index)
        rotate_cube(state, 'R', move_index)
    elif rotation_letter == 'L':
        state.face_move(move_index)
        state.swap(0, 4, 5, 2, 6, 2, 6, 6)
        state.swap(0, 4, 5, 2, 7, 3, 7, 7)
        state.swap(0, 4, 5, 2, 0, 4, 0, 0)
    elif rotation_letter == "L'":
        state.face_move_prime(move_index)
        state.swap(0, 2, 5, 4, 6, 6, 6, 2)
        state.swap(0, 2, 5, 4, 7, 7, 7, 3)
        state.swap(0, 2, 5, 4, 0, 0, 0, 4)
    elif rotation_letter == 'L2':
        rotate_cube(state, 'L', move_index)
        rotate_cube(state, 'L', move_index)
    elif rotation_letter == 'F':
        state.face_move(move_index)
        state.swap(0, 1, 5, 3, 4, 2, 0, 6)
        state.swap(0, 1, 5, 3, 5, 3, 1, 7)
        state.swap(0, 1, 5, 3, 6, 4, 2, 0)
    elif rotation_letter == "F'":
        state.face_move_prime(move_index)
        state.swap(0, 3, 5, 1, 4, 6, 0, 2)
        state.swap(0, 3, 5, 1, 5, 7, 1, 3)
        state.swap(0, 3, 5, 1, 6, 0, 2, 4)
    elif rotation_letter == 'F2':
        rotate_cube(state, 'F', move_index)
        rotate_cube(state, 'F', move_index)
    elif rotation_letter == 'B':
        state.face_move(move_index)
        state.swap(0, 3, 5, 1, 0, 2, 4, 6)
        state.swap(0, 3, 5, 1, 1, 3, 5, 7)
        state.swap(0, 3, 5, 1, 2, 4, 6, 0)
    elif rotation_letter == "B'":
        state.face_move_prime(move_index)
        state.swap(0, 1, 5, 3, 0, 6, 4, 2)
        state.swap(0, 1, 5, 3, 1, 7, 5, 3)
        state.swap(0, 1, 5, 3, 2, 0, 6, 4)
    elif rotation_letter == 'B2':
        rotate_cube(state, 'B', move_index)
        rotate_cube(state, 'B', move_index)


def scramble(gen_moves):
    cube = Cube()
    for i in gen_moves:
        rotate_cube(cube, i, moves.index(i[0]))
    cube.print_cube()
    return cube


if __name__ == '__main__':
    scrambled_cube, gen_moves = scramble_cube()
    output_cube = np.concatenate([np.array([colours_dict[i] for i in scrambled_cube.state[1]]),
                                  np.array([colours_dict[i]
                                           for i in scrambled_cube.state[2]]),
                                  np.array([colours_dict[i]
                                           for i in scrambled_cube.state[3]]),
                                  np.array([colours_dict[i]
                                           for i in scrambled_cube.state[4]]),
                                  np.array([colours_dict[i]
                                           for i in scrambled_cube.state[0]]),
                                  np.array([colours_dict[i] for i in scrambled_cube.state[5]])], axis=0)
    print_rubicks(output_cube)
    cube = Cube()
    cube.convert_from_np_array(output_cube)
    cube.print_cube()
