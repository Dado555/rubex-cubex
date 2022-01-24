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

        file_state = open('dataset_states_gen' + str(scramble) + ".bin", 'wb')
        pickle.dump(np.asarray(state_list), file_state)

        file_state.close()
        print("finished pickleing " + str(scramble))


#generate_dataset(10, 50000)
# open a file, where you stored the pickled data
file = open('dataset_states_gen0.bin', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()
