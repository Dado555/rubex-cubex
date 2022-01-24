from random import shuffle
import time
import random as rd
import pickle
from scramble_cube import *
from neural_network import *


def learning(num_of_cubes, max_number_of_scrambles, model):  # B, K, M
    positions_x = []
    moves_list = []
    for _ in range(num_of_cubes*12):
        positions_x.append(get_state_copy(starting_state))

    print("Finished generating complete list")

    for iteration_scr in range(1, max_number_of_scrambles+1):
        for state_idx in range(0, len(positions_x), 12):
            if len(moves_list) < len(positions_x):
                move = get_random_move(None)
                moves_list.append(move)
            else:
                move = get_random_move(moves_list[state_idx])
                moves_list[state_idx] = move

            rotate_cube(positions_x[state_idx], move, moves.index(move[0]))
            i = 1
            for m in moves_dict_for_possible[move]:
                new_move = get_state_copy(positions_x[state_idx])
                rotate_cube(new_move, m, moves.index(m[0]))
                positions_x[state_idx + i] = new_move
                i += 1

        print("Finished generating moves and their successors")
        # u ovom momentu generisane su sve pozicije nakon iteration scrambleovanja, kao i skup svih 11 (zbog ponistavanja) mogucih poteza nakon svake
        result_y = []
        positions_x_reformed = []

        for idx in range(0, len(positions_x), 12):
            positions_x_reformed.append(positions_x[idx])

            cube = positions_x[idx]
            y_vals = []
            y = -1
            for next_idx in range(1, 12):
                next_pos = positions_x[idx+next_idx]
                if check_if_final(next_pos):
                    y = 1
                    break

            # da li smo u finalnoj poziciji
            if y == 1:
                result_y.append(y)
                continue
            # ako nismo, uzimamo iz mreze
            y_vals = y = model(np.asarray(positions_x[idx+1:idx+12]))
            result_y.append(min(y_vals + 1))

        print("training epoche ")
        model.fit(np.asarray(positions_x_reformed, dtype=np.float32),
                  np.asarray(result_y, dtype=np.float32), batch_size=64, shuffle=False, epochs=200)

        print("scramble " + str(iteration_scr) + " finished")

    model_json = model.to_json()
    with open("model_rl_like.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model_rl_like.h5")
    print("Saved model to disk")
    print('djura')


model = create_NN()
learning(50000, 8, model)
