from scramble_cube import *
import pickle


def generate_dataset(num_of_scrambles, num_of_cubes):
    state_list = []
    moves_list = []

    for _ in range(num_of_cubes):
        state_list.append(get_state_copy(starting_state))

    for scramble in range(0, num_of_scrambles):
        for state_idx in range(0, len(state_list)):
            if len(moves_list) < len(state_list):
                move = get_random_move(None)
                moves_list.append(move)
            else:
                move = get_random_move(moves_list[state_idx])
                moves_list[state_idx] = move

            rotate_cube(state_list[state_idx], move, moves.index(move[0]))

        file_state = open('dataset_states_gen_100k_' + str(scramble) + ".bin", 'wb')
        pickle.dump(np.asarray(state_list), file_state)

        file_state.close()
        print("finished pickleing " + str(scramble))


def generate_dataset_2(num_of_scrambles, num_of_cubes):
    states_list = []
    moves_list = []
    state_list = []

    for _ in range(int(num_of_cubes/num_of_scrambles)):
        state_list.append(get_state_copy(starting_state))

    for scramble in range(0, num_of_scrambles):
        for state_idx in range(0, len(state_list)):
            if len(moves_list) < len(state_list):
                move = get_random_move(None)
                moves_list.append(move)
            else:
                move = get_random_move(moves_list[state_idx])
                moves_list[state_idx] = move

            rotate_cube(state_list[state_idx], move, moves.index(move[0]))

        states_list.extend(copy.deepcopy(state_list))

    file_state = open('data/dataset_states_gen_2_560_M.bin', 'wb')
    pickle.dump(np.asarray(states_list), file_state)

    file_state.close()
    print("finished pickleing")
    # print("finished pickleing " + str(scramble))


def add_scrambled_states(size, states_list):
    state_list = []
    moves_list = []

    for _ in range(size):
        state_list.append(get_state_copy(starting_state))

    for state_idx in range(0, len(state_list)):
        if len(moves_list) < len(state_list):
            move = get_random_move(None)
            moves_list.append(move)
        else:
            move = get_random_move(moves_list[state_idx])
            moves_list[state_idx] = move

        rotate_cube(state_list[state_idx], move, moves.index(move[0]))

    states_list.extend(copy.deepcopy(state_list))


def generate_dataset_3():
    states_list = []

    switcher = {
        0 : 10000,
        1 : 10000,
        2 : 10000,
        3 : 10000,
        4 : 47002,
        5 : 224818
    }
    
    for i in range(5):
        add_scrambled_states(switcher.get(i), states_list)

    for _ in range(11):
        add_scrambled_states(switcher.get(5), states_list)

    file_state = open('data/dataset_states_gen_2_560_M.bin', 'ab')
    pickle.dump(np.asarray(states_list), file_state)

    file_state.close()
    print("finished pickleing " + str(scramble))


# generate_dataset_3()
# generate_dataset(16, 160000)

# open a file, where you stored the pickled data
#file = open('data/dataset_states_gen_100k_0.bin', 'rb')

# dump information to that file
#data = pickle.load(file)

# close the file
#file.close()