import signal
import time

from keras.models import model_from_json

from greedy_search import *

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
    # json_file = open('model_rl_last_try.json', 'r')
    # loaded_model_json = json_file.read()
    # json_file.close()
    # loaded_model = model_from_json(loaded_model_json)
    # loaded_model.load_weights("model_rl_last_try.h5")
    # print("Loaded model from disk")
    #
    # loaded_model.compile(loss="mean_squared_error", optimizer="adam")
    #
    # json_file2 = open('model_rl_last_try2.json', 'r')
    # loaded_model_json2 = json_file2.read()
    # json_file2.close()
    # loaded_model2 = model_from_json(loaded_model_json2)
    # loaded_model2.load_weights("model_rl_last_try2.h5")
    # print("Loaded model from disk")
    #
    # loaded_model2.compile(loss="mean_squared_error", optimizer="adam")

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

    # 88/100  (10) (30s)  - model 22.5M
    # 86/100  (10) (30s)  - model 2.5M
    # 274 : 265  (10) (30s)  - model 2.5M : model 22.5M

    #   100 iteracija, 30s time out
    # 1 scramble - 100 : 100 : 100 : 100
    # 2 scrambles - 100 : 90 : 100 : 100
    # 3 scrambles - 100 : 97 : 100 : 100
    # 4 scrambles - 100 : 93 : 100 : 100
    # 5 scrambles - 100 : 95 : 100 : 100
    # 6 scrambles - 100 : 97 : 100 : 100
    # 7 scrambles - 100 : 96 : 100 : 100    RL3 = 100; RL4 = 100;
    # 8 scrambles - 100 : 96 : 100 : 100    RL3 = 100; RL4 = 100;
    # 9 scrambles - 89  : 90 : 100 : 100    RL3 = 100; RL4 = 100;
    # 10 scrambles - 86 : 88 : 97 : 98      RL3 = 100; RL4 = 100;

    #   50 iteracija, 30s time out
    # 11 scrambles - 30 : 37 : 41 : 48      RL3 = 47; RL4 = 47;
    # 12 scrambles -           40 : 38      RL3 = ; RL4 = ;
    # 13 scrambles -
    # 14 scrambles -
    # 15 scrambles -
    # 6: 8

    x, y, z, k = 0, 0, 0, 0
    for i in range(30):
        print("Iteration " + str(i) + ". : ")

        moves_for_gen = get_random_moves_no_recur(11)
        print("state to solve: " + str(moves_for_gen))
        print("---------------------------------------")

        cube = get_state_copy(starting_state)
        for m in moves_for_gen:
            rotate_cube(cube, m, moves.index(m[0]))

        # init_search_state = get_state_copy(cube)
        # print("starting search (RL1)")
        # signal.signal(signal.SIGALRM, signal_handler)
        # signal.alarm(30)  # Ten seconds
        # try:
        #     result = all_star(init_search_state, loaded_model)
        #     print("result (RL1): " + str(result))
        #     x += 1
        # except Exception:
        #     print("Timed out (RL1)!")
        #
        # init_search_state = get_state_copy(cube)
        # print("starting search (RL2)")
        # signal.signal(signal.SIGALRM, signal_handler)
        # signal.alarm(30)  # Ten seconds
        # try:
        #     result = all_star(init_search_state, loaded_model2)
        #     print("result (RL2): " + str(result))
        #     y += 1
        # except Exception:
        #     print("Timed out (RL2)!")

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
