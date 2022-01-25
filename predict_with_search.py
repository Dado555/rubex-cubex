import signal
import time

from keras.models import model_from_json

from greedy_search import *

if __name__ == "__main__":
    json_file3 = open('model_rl_last_try3.json', 'r')
    loaded_model_json3 = json_file3.read()
    json_file3.close()
    loaded_model3 = model_from_json(loaded_model_json3)
    loaded_model3.load_weights("model_rl_last_try3.h5")
    print("Loaded model from disk")

    loaded_model3.compile(loss="mean_squared_error", optimizer="adam")

    json_file4 = open('model_rl_last_try4.json', 'r')
    loaded_model_json4 = json_file4.read()
    json_file4.close()
    loaded_model4 = model_from_json(loaded_model_json4)
    loaded_model4.load_weights("model_rl_last_try4.h5")
    print("Loaded model from disk")

    loaded_model3.compile(loss="mean_squared_error", optimizer="adam")

    x, y, z, k = 0, 0, 0, 0
    for i in range(30):
        print("Iteration " + str(i) + ". : ")

        moves_for_gen = get_random_moves_no_recur(11)
        print("state to solve: " + str(moves_for_gen))
        print("---------------------------------------")

        cube = get_state_copy(starting_state)
        for m in moves_for_gen:
            rotate_cube(cube, m, moves.index(m[0]))

        init_search_state = get_state_copy(cube)
        print("starting search (RL3)")
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(60)  # Ten seconds
        try:
            result = all_star(init_search_state, loaded_model3)
            print("result (RL3): " + str(result))
            z += 1
        except Exception:
            print("Timed out (RL3)!")

        init_search_state = get_state_copy(cube)
        print("starting search (RL4)")
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(60)  # Ten seconds
        try:
            result = all_star(init_search_state, loaded_model4)
            print("result (RL4): " + str(result))
            k += 1
        except Exception:
            print("Timed out (RL4)!")

        print(" score = " + str(x) + " : " + str(y) + " : " + str(z) + " : " + str(k))
        print("************************************")

    # print("Score = " + str(x) + " : " + str(y))
