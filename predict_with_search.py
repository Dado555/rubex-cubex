from keras.models import model_from_json
from scramble_cube import *
import numpy as np
from a_star import *

if __name__ == "__main__":
    json_file = open('kaggle_model/supervised_2/model2_rl.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("kaggle_model/supervised_2/model2_rl.h5")
    print("Loaded model from disk")

    loaded_model.compile(loss="mean_squared_error", optimizer="adam")

    moves_for_gen = gen_random_moves(7)
    print(moves_for_gen)
    cube = get_state_copy(starting_state)
    for m in moves_for_gen:
        rotate_cube(cube, m, moves.index(m[0]))

    init_search_state = get_state_copy(cube)
    print("starting search")
    result = all_star(init_search_state, loaded_model)
    print(result)
