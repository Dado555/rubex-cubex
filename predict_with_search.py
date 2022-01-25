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

    # json_file = open('model_rl3.json', 'r')
    # loaded_model_json = json_file.read()
    # json_file.close()
    # loaded_model = model_from_json(loaded_model_json)
    # loaded_model.load_weights("model_rl3.json.h5")
    # print("Loaded model from disk")
    #
    # loaded_model.compile(loss="mean_squared_error", optimizer="adam")
    #
    # json_file1 = open('model_rl4.json', 'r')
    # loaded_model_json1 = json_file1.read()
    # json_file1.close()
    # loaded_model1 = model_from_json(loaded_model_json1)
    # loaded_model1.load_weights("model_rl4.json.h5")
    # print("Loaded model from disk")
    #
    # loaded_model1.compile(loss="mean_squared_error", optimizer="adam")
    #
    # json_file2 = open('model_rl5.json', 'r')
    # loaded_model_json2 = json_file2.read()
    # json_file2.close()
    # loaded_model2 = model_from_json(loaded_model_json2)
    # loaded_model2.load_weights("model_rl5.json.h5")
    # print("Loaded model from disk")
    #
    # loaded_model2.compile(loss="mean_squared_error", optimizer="adam")
    #
    # # moves_list = ["U'", "R'", "U'", "B'", 'F', 'L', "R'", 'L', "U'", "B'"]
    # # cube = get_state_copy(starting_state)
    # # for m in moves_list:
    # #     rotate_cube(cube, m, moves.index(m[0]))
    #
    # x_sc, y_sc, z_sc = 0, 0, 0
    #
    # for i in range(20):
    #     print("\n" + str(i) + ". SCRAMBLE (MODEL 1): \n")
    #
    #     moves_for_gen = get_random_moves_no_recur(11)
    #     print("state to solve: "+ str(moves_for_gen))
    #     cube = get_state_copy(starting_state)
    #     for m in moves_for_gen:
    #         rotate_cube(cube, m, moves.index(m[0]))
    #
    #     init_search_state = get_state_copy(cube)
    #     print("starting search")
    #
    #     signal.signal(signal.SIGALRM, signal_handler)
    #     signal.alarm(20)   # Ten seconds
    #     try:
    #         result = all_star(init_search_state, loaded_model)
    #         print("result: " + str(result))
    #         x_sc += 1
    #     except Exception:
    #         print("Timed out!")
    #
    #     print("\n" + str(i) + ". SCRAMBLE (MODEL 2): \n")
    #     print("state to solve: "+ str(moves_for_gen))
    #     init_search_state = get_state_copy(cube)
    #     print("starting search 1")
    #
    #     signal.signal(signal.SIGALRM, signal_handler)
    #     signal.alarm(20)   # Ten seconds
    #     try:
    #         result = all_star(init_search_state, loaded_model1)
    #         print("result 1: " + str(result))
    #         y_sc += 1
    #     except Exception:
    #         print("Timed out 1!")
    #
    #     print("\n" + str(i) + ". SCRAMBLE (MODEL 3): \n")
    #     print("state to solve: "+ str(moves_for_gen))
    #     init_search_state = get_state_copy(cube)
    #     print("starting search 2")
    #
    #     signal.signal(signal.SIGALRM, signal_handler)
    #     signal.alarm(20)   # Ten seconds
    #     try:
    #         result = all_star(init_search_state, loaded_model2)
    #         print("result 2: " + str(result))
    #         z_sc += 1
    #     except Exception:
    #         print("Timed out 2!")
    #
    # print("\n\nScore: " + str(x_sc) + " : " + str(y_sc) + " : " + str(z_sc))

    init_search_state = get_state_copy(starting_state)
    print_cube(init_search_state)
    print("R")
    rotate_cube(init_search_state, "R", moves.index("R"))
    print_cube(init_search_state)
    print("L")
    rotate_cube(init_search_state, "L", moves.index("L"))
    print_cube(init_search_state)
    print("U'")
    rotate_cube(init_search_state, "U'", moves.index("U"))
    print_cube(init_search_state)
    print("D")
    rotate_cube(init_search_state, "D", moves.index("D"))
    print_cube(init_search_state)
    print("R")
    rotate_cube(init_search_state, "R", moves.index("R"))
    print_cube(init_search_state)
    print("F")
    rotate_cube(init_search_state, "F", moves.index("F"))
    print_cube(init_search_state)
    print("F")
    rotate_cube(init_search_state, "F", moves.index("F"))
    print_cube(init_search_state)
    print("U")
    rotate_cube(init_search_state, "U", moves.index("U"))
    print_cube(init_search_state)
    print("B")
    rotate_cube(init_search_state, "B", moves.index("B"))
    print_cube(init_search_state)
    print("R'")
    rotate_cube(init_search_state, "R'", moves.index("R"))
    print_cube(init_search_state)
    print("D'")
    rotate_cube(init_search_state, "D'", moves.index("D"))
    print_cube(init_search_state)
    print("L'")
    rotate_cube(init_search_state, "L'", moves.index("L"))
    print_cube(init_search_state)
    print("B'")
    rotate_cube(init_search_state, "B'", moves.index("B"))
    print_cube(init_search_state)
    print("F'")
    rotate_cube(init_search_state, "F'", moves.index("F"))
    print_cube(init_search_state)


    # for i in range(10):
    #     moves_for_gen = get_random_moves_no_recur(10)
    #     print("state to solve: "+ str(moves_for_gen))
    #     cube = get_state_copy(starting_state)
    #     for m in moves_for_gen:
    #         rotate_cube(cube, m, moves.index(m[0]))

    #     init_search_state = get_state_copy(cube)
    #     print("starting search")
    #     result = all_star(init_search_state, loaded_model)
    #     print("result: " + str(result))
