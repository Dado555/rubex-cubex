import random
import numpy as np
from rubicks_visualize_console import *
import copy

moves = ["U", "L", "F", "R", "B", "D",
         "U'", "L'", "F'", "R'", "B'", "D'"]

colours_dict = {
    'w': white_center_sq,
    'o': orange_center_sq,
    'r': red_center_sq,
    'g': green_center_sq,
    'b': blue_center_sq,
    'y': yellow_center_sq
}

starting_state = [
    # prva strana, bela u sredini
    0, 0, 0, 0, 1, 0,
    0, 0, 0, 0, 1, 0,
    0, 0, 0, 0, 1, 0,
    0, 0, 0, 0, 1, 0,
    0, 0, 0, 0, 1, 0,
    0, 0, 0, 0, 1, 0,
    0, 0, 0, 0, 1, 0,
    0, 0, 0, 0, 1, 0,
    # druga strana, narandzasta
    1, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0,
    # treca strana, zelena u sredini
    0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0,
    # cetvrta strana, crvena u sredini
    0, 0, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 0,
    # peta strana, plava u sredini
    0, 0, 0, 1, 0, 0,
    0, 0, 0, 1, 0, 0,
    0, 0, 0, 1, 0, 0,
    0, 0, 0, 1, 0, 0,
    0, 0, 0, 1, 0, 0,
    0, 0, 0, 1, 0, 0,
    0, 0, 0, 1, 0, 0,
    0, 0, 0, 1, 0, 0,
    # sesta strana, zuta u sredini
    0, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1,
]


def conv(array):
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


def scramble_cube(moves_num):
    # random 25 do 30 poteza za mjesanje kocke
    # moves_num = random.randint(25, 30)
    gen_moves = [random.choice(moves) for i in range(moves_num)]
    return scramble(gen_moves), gen_moves


finish_state = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
                ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'], [
    'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']]


def face_move_prime(state, x):
    x = 6*8*x
    state[x: x + 6], state[x + 12: x+18], state[x + 42: x + 48], state[x + 30: x + 36] = \
        state[x + 12: x + 18], state[x + 42: x +
                                     48], state[x + 30: x + 36], state[x: x + 6]
    state[x + 6:x + 12], state[x + 24: x + 30], state[x + 36: x + 42], state[x + 18: x + 24] = \
        state[x + 24: x + 30], state[x + 36: x +
                                     42], state[x + 18: x + 24], state[x + 6:x + 12]

    # state[x: x + 6], state[x + 36: x + 42], state[x + 24: x + 30], state[x + 12: x+18] = \
    #     state[x + 36: x + 42], state[x + 24: x + 30], state[x + 12: x+18], state[x: x + 6]
    # state[x + 6:x + 12], state[x + 42: x + 48], state[x + 30: x + 36], state[x + 18: x + 24] = \
    #     state[x + 42: x + 48], state[x + 30: x + 36], state[x + 18: x + 24], state[x + 6:x + 12]


def face_move(state, x):
    x = 6*8*x
    state[x: x + 6], state[x + 12: x+18], state[x + 42: x + 48], state[x + 30: x + 36] = \
        state[x + 30: x + 36], state[x: x +
                                     6], state[x + 12: x+18], state[x + 42: x + 48]
    state[x + 6:x + 12], state[x + 24: x + 30], state[x + 36: x + 42], state[x + 18: x + 24] = \
        state[x + 18: x + 24], state[x + 6:x +
                                     12], state[x + 24: x + 30], state[x + 36: x + 42]

    # state[x: x + 6], state[x + 12: x+18], state[x + 24: x + 30], state[x + 36: x + 42] = \
    #     state[x + 12: x + 18], state[x + 24: x + 30], state[x + 36: x + 42], state[x: x + 6]
    # state[x + 6:x + 12], state[x + 18: x + 24], state[x + 30: x + 36], state[x + 42: x + 48] = \
    #     state[x + 18: x + 24], state[x + 30: x + 36], state[x + 42: x + 48], state[x + 6:x + 12]


def swap(state, x1, x2, x3, x4, y1, y2, y3, y4):
    index_1 = 8*6*x1
    index_2 = 8*6*x2
    index_3 = 8*6*x3
    index_4 = 8*6*x4

    x1y1 = index_1 + 6*y1
    x2y2 = index_2 + 6*y2
    x3y3 = index_3 + 6*y3
    x4y4 = index_4 + 6*y4

    state[x1y1:x1y1 + 6], state[x2y2:x2y2 + 6], state[x3y3:x3y3 + 6], state[x4y4:x4y4 + 6] = \
        state[x2y2:x2y2 + 6], state[x3y3:x3y3 +
                                    6], state[x4y4:x4y4 + 6], state[x1y1:x1y1 + 6]


def get_state_copy(state):
    return copy.deepcopy(state)


def print_cube(state):
    print(
        "    " + conv(state[0:6]) + conv(state[6:12]) + conv(state[12:18]) + "\n" +
        "    " + conv(state[18:24]) + "w" + conv(state[24:30]) + "\n" +
        "    " + conv(state[30:36]) + conv(state[36:42]) + conv(state[42:48]) + "\n\n" +

        conv(state[48:54]) + conv(state[54:60]) + conv(state[60:66]
                                                       ) + " " + conv(state[96:102]) + conv(state[102:108])
        + conv(state[108:114]) + " " + conv(state[144:150]) + conv(state[150:156]) + conv(state[156:162]) + " " + conv(state[192:198]) +
        conv(state[198:204]) + conv(state[204:210]) + "\n" +

        conv(state[66:72]) + "o" + conv(state[72:78]) + " " + conv(state[114:120]) + "g" + conv(state[120:126]) + " " +
        conv(state[162:168]) + "r" + conv(state[168:174]) + " " + conv(state[210:216]) + "b" + conv(state[216:222]) + "\n" +

        conv(state[78:84]) + conv(state[84:90]) + conv(state[90:96]) + " " + conv(state[126:132]) + conv(state[132:138]) +
        conv(state[138:144]) + " " + conv(state[174:180]) + conv(state[180:186]) + conv(state[186:192]) + " " + conv(state[222:228]) +
        conv(state[228:234]) + conv(state[234:240]) + "\n\n" +

        "    " + conv(state[240:246]) + conv(state[246:252]) + conv(state[252:258]) + "\n" +
        "    " + conv(state[258:264]) + "y" + conv(state[264:270]) + "\n" +
        "    " + conv(state[270:276]) +
        conv(state[276:282]) + conv(state[282:288]) + "\n"
    )


def check_if_final(state):
    for i in range(0, len(starting_state)):
        if state[i] != starting_state[i]:
            return False
    return True
    # for i in range(0, 6):
    #     for j in range(0, 8):
    #         if state[i][j] != finish_state[i][j]:
    #             return False
    # return True


def convert_from_np_array(state, np_array):
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

        sqr_color = conv(np_array[side])
        state[state_row][side % 8] = sqr_color

        if side % 8 == 7:
            iter += 8


def convert_to_np_array(state):
    return np.concatenate([np.array([colours_dict[i] for i in state[1]]),
                           np.array([colours_dict[i] for i in state[2]]),
                           np.array([colours_dict[i] for i in state[3]]),
                           np.array([colours_dict[i] for i in state[4]]),
                           np.array([colours_dict[i] for i in state[0]]),
                           np.array([colours_dict[i] for i in state[5]])], axis=0)


def convert_to_array_for_nn(state):
    array1 = np.concatenate([colours_dict[i] for i in state[1]])
    array2 = np.concatenate([colours_dict[i] for i in state[2]])
    array3 = np.concatenate([colours_dict[i] for i in state[3]])
    array4 = np.concatenate([colours_dict[i] for i in state[4]])
    array5 = np.concatenate([colours_dict[i] for i in state[0]])
    array6 = np.concatenate([colours_dict[i] for i in state[5]])
    ret = np.concatenate(
        [array1, array2, array3, array4, array5, array6], axis=0)
    return np.expand_dims(ret, axis=0)


def rotate_cube(state, rotation_letter, move_index):
    if rotation_letter == 'U':  # works
        face_move(state, move_index)
        swap(state, 1, 2, 3, 4, 0, 0, 0, 0)
        swap(state, 1, 2, 3, 4, 1, 1, 1, 1)
        swap(state, 1, 2, 3, 4, 2, 2, 2, 2)
    elif rotation_letter == "U'":  # works
        face_move_prime(state, move_index)
        swap(state, 1, 4, 3, 2, 0, 0, 0, 0)
        swap(state, 1, 4, 3, 2, 1, 1, 1, 1)
        swap(state, 1, 4, 3, 2, 2, 2, 2, 2)
    elif rotation_letter == 'U2':
        rotate_cube(state, 'U', move_index)
        rotate_cube(state, 'U', move_index)
    elif rotation_letter == 'D':  # works
        face_move(state, move_index)
        swap(state, 1, 4, 3, 2, 5, 5, 5, 5)
        swap(state, 1, 4, 3, 2, 6, 6, 6, 6)
        swap(state, 1, 4, 3, 2, 7, 7, 7, 7)
    elif rotation_letter == "D'":  # works
        face_move_prime(state, move_index)
        swap(state, 1, 2, 3, 4, 5, 5, 5, 5)
        swap(state, 1, 2, 3, 4, 6, 6, 6, 6)
        swap(state, 1, 2, 3, 4, 7, 7, 7, 7)
    elif rotation_letter == 'D2':
        rotate_cube(state, 'D', move_index)
        rotate_cube(state, 'D', move_index)
    elif rotation_letter == 'R':  # works
        face_move(state, move_index)
        swap(state, 0, 2, 5, 4, 2, 2, 2, 2)
        swap(state, 0, 2, 5, 4, 4, 4, 4, 4)
        swap(state, 0, 2, 5, 4, 7, 7, 7, 7)
    elif rotation_letter == "R'":  # works
        face_move_prime(state, move_index)
        swap(state, 0, 4, 5, 2, 2, 2, 2, 2)
        swap(state, 0, 4, 5, 2, 4, 4, 4, 4)
        swap(state, 0, 4, 5, 2, 7, 7, 7, 7)
    elif rotation_letter == 'R2':
        rotate_cube(state, 'R', move_index)
        rotate_cube(state, 'R', move_index)
    elif rotation_letter == 'L':  # works
        face_move(state, move_index)
        swap(state, 0, 4, 5, 2, 0, 0, 0, 0)
        swap(state, 0, 4, 5, 2, 3, 3, 3, 3)
        swap(state, 0, 4, 5, 2, 5, 5, 5, 5)
    elif rotation_letter == "L'":  # works
        face_move_prime(state, move_index)
        swap(state, 0, 2, 5, 4, 0, 0, 0, 0)
        swap(state, 0, 2, 5, 4, 3, 3, 3, 3)
        swap(state, 0, 2, 5, 4, 5, 5, 5, 5)
    elif rotation_letter == 'L2':
        rotate_cube(state, 'L', move_index)
        rotate_cube(state, 'L', move_index)
    elif rotation_letter == 'F':  # works
        face_move(state, move_index)
        swap(state, 0, 1, 5, 3, 5, 7, 2, 0)  # 5 7 2 0    4, 2, 0, 6
        swap(state, 0, 1, 5, 3, 6, 4, 1, 3)  # 6 4 1 3    5, 3, 1, 7
        swap(state, 0, 1, 5, 3, 7, 2, 0, 5)  # 7 2 0 5    6, 4, 2, 0
    elif rotation_letter == "F'":  # works
        face_move_prime(state, move_index)
        swap(state, 0, 3, 5, 1, 5, 0, 2, 7)  # 5 0 2 7    4, 6, 0, 2
        swap(state, 0, 3, 5, 1, 6, 3, 1, 4)  # 6 3 1 4    5, 7, 1, 3
        swap(state, 0, 3, 5, 1, 7, 5, 0, 2)  # 7 5 0 2    6, 0, 2, 4
    elif rotation_letter == 'F2':
        rotate_cube(state, 'F', move_index)
        rotate_cube(state, 'F', move_index)
    elif rotation_letter == 'B':  # works
        face_move_prime(state, move_index)
        swap(state, 0, 3, 5, 1, 0, 2, 7, 5)  # 0, 2, 7, 5    0, 2, 4, 6
        swap(state, 0, 3, 5, 1, 1, 4, 6, 3)  # 1, 4, 6, 3    1, 3, 5, 7
        swap(state, 0, 3, 5, 1, 2, 7, 5, 0)  # 2, 7, 5, 0    2, 4, 6, 0
    elif rotation_letter == "B'":  # works
        face_move(state, move_index)
        swap(state, 0, 1, 5, 3, 0, 5, 7, 2)  # 0, 5, 7, 2    0, 6, 4, 2
        swap(state, 0, 1, 5, 3, 1, 3, 6, 4)  # 1, 3, 6, 4    1, 7, 5, 3
        swap(state, 0, 1, 5, 3, 2, 0, 5, 7)  # 2, 0, 5, 7    2, 0, 6, 4
    elif rotation_letter == 'B2':
        rotate_cube(state, 'B', move_index)
        rotate_cube(state, 'B', move_index)


def get_oposite(move):
    if len(move) == 1:
        return moves[moves.index(move[0]) + 6]
    else:
        return moves[moves.index(move[0])]


def scramble(gen_moves):
    cube = get_state_copy(starting_state)
    print(gen_moves)
    print(gen_moves[::-1])
    print([get_oposite(i) for i in gen_moves[::-1]])

    for i in gen_moves:
        rotate_cube(cube, i, moves.index(i[0]))
        print('Move: ' + i)
        print_cube(cube)

    print("***************")
    print("SOLVING CUBE: ")
    print("***************")

    # get oposite moves for reversed list of moves, to solve cube
    for i in gen_moves[::-1]:
        rotate_cube(cube, get_oposite(i), moves.index(i[0]))
        print("Move: " + get_oposite(i))
        print_cube(cube)

    return cube


if __name__ == '__main__':
    scramble_cube(20)
    # rotate_cube(starting_state, "B'", 3)
    # print_cube(starting_state)
    # scrambled_cube, gen_moves = scramble_cube()
    # output_cube = np.concatenate([np.array([colours_dict[i] for i in scrambled_cube[1]]),
    #                               np.array([colours_dict[i] for i in scrambled_cube[2]]),
    #                               np.array([colours_dict[i] for i in scrambled_cube[3]]),
    #                               np.array([colours_dict[i] for i in scrambled_cube[4]]),
    #                               np.array([colours_dict[i] for i in scrambled_cube[0]]),
    #                               np.array([colours_dict[i] for i in scrambled_cube[5]])], axis=0)
    # print_rubicks(output_cube)
    #
    # new_cube = get_state_copy(finish_state)
    # convert_from_np_array(new_cube, output_cube)
    # print_cube(new_cube)
