from keras.models import model_from_json
from scramble_cube import *
import numpy as np
from a_star import *
import signal

'''
    ["U'", "R'", "U'", "B'", 'F', 'L', "R'", 'L', "U'", "B'"]

    43 / 50 , 40 / 50 za 10
    15(13) / 20 , 17(14) / 20 za 11
    14 / 20 , 13 / 20 za 12

    16 : 13 : 17 (od 20) za 10
    12 : 13 : 12 (od 20) za 11      13 : 10 : 13
'''

def signal_handler(signum, frame):
    raise Exception("Timed out!")


if __name__ == "__main__":

    json_file = open('model_rl.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model_rl.json.h5")
    print("Loaded model from disk")

    loaded_model.compile(loss="mean_squared_error", optimizer="adam")

    json_file1 = open('model_rl2.json', 'r')
    loaded_model_json1 = json_file1.read()
    json_file1.close()
    loaded_model1 = model_from_json(loaded_model_json1)
    loaded_model1.load_weights("model_rl2.json.h5")
    print("Loaded model from disk")

    loaded_model1.compile(loss="mean_squared_error", optimizer="adam")

    # state = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    #  0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    #  0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
    #  0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #  1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
    #  0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
    #  0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
    #  0, 0, 0, 0, 1, 0, 0, 0, 0,
    #  0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    # print_cube(state)
    # print("starting search")
    # result = all_star(state, loaded_model)
    # print("result: " + str(result))

    x, y = 0, 0
    # 88/100  (10) (30s)  - model 22.5M
    # 86/100  (10) (30s)  - model 2.5M

    for i in range(300):
        print("Iteration " + str(i) + ". : ")

        moves_for_gen = get_random_moves_no_recur(10)
        print("state to solve: " + str(moves_for_gen))
        print("---------------------------------------")

        cube = get_state_copy(starting_state)
        for m in moves_for_gen:
            rotate_cube(cube, m, moves.index(m[0]))

        init_search_state = get_state_copy(cube)
        print("starting search")
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(30)   # Ten seconds
        try:
            result = all_star(init_search_state, loaded_model)
            print("result: " + str(result))
            x += 1
        except Exception:
            print("Timed out!")

        init_search_state = get_state_copy(cube)
        print("starting search 2")
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(30)  # Ten seconds
        try:
            result = all_star(init_search_state, loaded_model1)
            print("result 2: " + str(result))
            y += 1
        except Exception:
            print("Timed out 2!")

        print("************************************")

    print("Score = " + str(x) + " : " + str(y))
