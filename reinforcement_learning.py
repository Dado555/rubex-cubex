from random import shuffle

import numpy as np

from scramble_cube import *
from neural_network import *
import time


def learning(batch_size, max_number_of_scrambles, training_iters, model):  # B, K, M
    '''
    θ←initialize_parameters()
    θe←θ
    for m=1 to M do
    X←get_scrambled_states(B, K)
    for xi∈X do
    ← + θ y g min ( ( , x A( , x a)) j A( (x a, ))) i a
    a
    i i i e θ ← θ , loss train( , j X, )y
    if (M mod C=0) and (loss<ϵ) then
    θe
    '''
    for iteration in range(0, training_iters):
        positions_x = []  # niz np array-ova
        for b in range(0, batch_size):  # ako je 25
            moves_for_gen = gen_random_moves(max_number_of_scrambles)
            cube = get_state_copy(starting_state)
            positions = []  # njih ce biti 32
            for m in moves_for_gen:
                rotate_cube(cube, m, moves.index(m[0]))
                positions.append(get_state_copy(cube))

            positions_x.extend(positions)

        #result_y = [None] * batch_size * max_number_of_scrambles
        result_y = []
        positions_x_reformed = []
        #positions_x_reformed = [None] * batch_size * max_number_of_scrambles
        i = 0
        j = 0
        for x in range(0, len(positions_x)):
            if x % max_number_of_scrambles == 0:
                i += 1
            cube = positions_x[x]
            init_state = get_state_copy(cube)
            y_from_moves = []
            for m in moves:
                rotate_cube(cube, m, moves.index(m[0]))
                if check_if_final(cube):
                    j += 1
                    y_from_moves.append(0)
                    break
                else:
                    y = model(np.expand_dims(cube, axis=0))
                    y_from_moves.append(abs(y))
                cube = get_state_copy(init_state)  # vracamo

            min_y = min(y_from_moves)
            positions_x_reformed.append(np.array(cube))
            result_y.append(min_y*100)
            # positions_x_reformed[(x % max_number_of_scrambles)*batch_size + i - 1] = np.asarray(cube)
            # result_y[(x % max_number_of_scrambles)*batch_size + i - 1] = min_y * 100

            # i += 1
            # print("current iter: " + str(i) +
            #       ", y value is: " + str(min(y_from_moves)))
        print("final checks: " + str(j))
        print("training epoche ")
        model.fit(np.asarray(positions_x_reformed, dtype=np.float32),
                  np.asarray(result_y, dtype=np.float32), batch_size=25, shuffle=False, epochs=1000)

    model_json = model.to_json()
    with open("model_rl.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model_rl.json.h5")
    print("Saved model to disk")
    print('djura')


if __name__ == '__main__':
    model = create_NN()
    # array = np.array([i for i in range(0, 288)])
    # array = np.expand_dims(array, axis=0)
    # print(model.predict(array))
    learning(20000, 25, 1, model)
