from random import shuffle
import time
import random as rd
import pickle
from scramble_cube import *
from neural_network import *


def learning(num_of_cubes, max_number_of_scrambles, model):  # B, K, M
    positions_x = []

    for _ in range(num_of_cubes):
        moves_to_make = gen_random_moves(max_number_of_scrambles)

        new_move = get_state_copy(starting_state)
        for m in moves_to_make:
            rotate_cube(new_move, m, moves.index(m[0]))
            positions_x.append(get_state_copy(new_move))

            for og_m in moves:
                new_move2 = get_state_copy(new_move)
                rotate_cube(new_move2, og_m, moves.index(og_m[0]))
                positions_x.append(new_move2)

    print("Finished generating moves and their successors")
    # u ovom momentu generisane su sve pozicije nakon iteration scrambleovanja, kao i skup svih 11 (zbog ponistavanja) mogucih poteza nakon svake
    result_y = []
    positions_x_reformed = []

    print("calculating predictions")
    # racunamo sve y, ubrzavamo, nadam se
    calculate_y_from_nn = model.predict(
        np.asarray(positions_x), batch_size=4096)
    print("finished calc pred")

    for idx in range(0, len(positions_x), 13):
        positions_x_reformed.append(positions_x[idx])

        cube = positions_x[idx]
        y_vals = []
        y = -1
        for next_idx in range(1, 13):
            next_pos = positions_x[idx+next_idx]
            if check_if_final(next_pos):
                y = 1
                break

        # da li smo u finalnoj poziciji
        if y == 1:
            result_y.append(y)
            continue
        # ako nismo, uzimamo iz mreze
        y_vals = calculate_y_from_nn[idx+1:idx+13]
        result_y.append(min(y_vals)+1)

    print("training epoche ")
    model.fit(np.asarray(positions_x_reformed, dtype=np.float32),
              np.asarray(result_y, dtype=np.float32), batch_size=256, shuffle=True, epochs=50)

    model_json = model.to_json()
    with open("models/model_rl_final.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("models/model_rl_final.h5")
    print("Saved model to disk")
    print('djura')


json_file = open('models/model_sl_final.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights('models/model_sl_final.json.h5')
print("Loaded model from disk")

model.compile(loss="mean_squared_error", optimizer="adam")
model.summary()
#model = create_NN()
print("iteracija 1 ~~~~")
learning(50000, 20, model) # 2000000
