from keras.models import model_from_json
from scramble_cube import *
import numpy as np

if __name__ == "__main__":
    json_file = open('model_rl.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model_rl.json.h5")
    print("Loaded model from disk")

    loaded_model.compile(loss="mean_squared_error", optimizer="adam")

    moves_for_gen = gen_random_moves(25)
    cube = get_state_copy(starting_state)
    positions = []  # njih ce biti 25
    for m in moves_for_gen:
        rotate_cube(cube, m, moves.index(m[0]))
        positions.append(get_state_copy(cube))

    predicted = loaded_model.predict(np.asarray(positions))
    print(predicted)
