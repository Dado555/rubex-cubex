from random import shuffle
from scramble_cube import *
from neural_network import *
import time
import random as rd
import pickle


def learning(num_of_cubes, max_number_of_scrambles, model):  # B, K, M
    for iteration in range(1, max_number_of_scrambles+1):
        positions_x = []

        for _ in range(0, num_of_cubes):
            # dobijamo samo random niz koji nema direktnu rekurziju (potez pa njegov prim)
            moves_for_gen = get_random_moves_no_recur(iteration)
            cube = get_state_copy(starting_state)
            last_move = None
            for m in moves_for_gen:
                rotate_cube(cube, m, moves.index(m[0]))
                last_move = m

            # odabrana pozicija (nakon iteration broj scrambleovanja)
            positions_x.append(cube)
            # dobavljamo sve poteze osim onog koji ponistava prethodni odigrani
            for m in moves_dict_for_possible[last_move]:
                new_move = get_state_copy(cube)
                rotate_cube(new_move, m, moves.index(m[0]))
                positions_x.append(new_move)

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
                  np.asarray(result_y, dtype=np.float32), batch_size=32, shuffle=False, epochs=100)

        print("scramble " + str(iteration) + " finished")

    model_json = model.to_json()
    with open("model_rl_like.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model_rl_like.h5")
    print("Saved model to disk")
    print('djura')


if __name__ == '__main__':
    # json_file = open('kaggle_model/supervised_2/model2_rl.json', 'r')
    # loaded_model_json = json_file.read()
    # json_file.close()
    # model = model_from_json(loaded_model_json)
    # model.load_weights("kaggle_model/supervised_2/model2_rl.h5")
    # model.compile(loss="mean_squared_error", optimizer="adam")
    # model.summary()
    # print("Loaded model from disk")
    model = create_NN()
    learning(1000, 10, model)
