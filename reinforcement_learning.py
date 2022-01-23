from random import shuffle
from scramble_cube import *
from neural_network import *
import time
import random as rd
import pickle


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
        # positions_x = []
        # result_y = []
        # file_state = open('dataset_states.bin', 'wb')
        # file_res = open('dataset_results.bin', 'wb')
        # j = 0
        # for b in range(0, batch_size):
        #     if j % 1000 == 0:
        #         print(str(j) + "/" + str(batch_size*max_number_of_scrambles))
        #     cube = get_state_copy(starting_state)
        #     for i in range(0, max_number_of_scrambles):
        #         rand_move = rd.choice(moves)
        #         rotate_cube(cube, rand_move, moves.index(rand_move[0]))
        #         positions_x.append(np.array(get_state_copy(cube)))
        #         result_y.append(rand_move)
        #         j += 1
        # pickle.dump(positions_x, file_state)
        # pickle.dump(result_y, file_res)

        # file_state.close()
        # file_res.close()
        # print("finished pickleing")
        # print("training epoche ")
        # model.fit(np.asarray(positions_x, dtype=np.float32),
        #           np.asarray(result_y, dtype=np.float32), batch_size=32, epochs=100)

        positions_x = []  # niz np array-ova
        for b in range(0, batch_size):  # ako je 32
            moves_for_gen = gen_random_moves(max_number_of_scrambles)
            cube = get_state_copy(starting_state)
            positions = []  # njih ce biti 25
            for m in moves_for_gen:
                rotate_cube(cube, m, moves.index(m[0]))
                positions.append(get_state_copy(cube))

            positions_x.extend(positions)

        result_y = []

        positions_x_reformed = []
        i = 0
        for x in positions_x:
            cube = x
            init_state = get_state_copy(cube)
            y_from_moves = []
            for m in moves:
                rotate_cube(cube, m, moves.index(m[0]))
                if check_if_final(cube):
                    y_from_moves.append(0)
                    break
                else:
                    y = model(np.expand_dims(cube, axis=0))
                    if y != 0:
                        y_from_moves.append(abs(y))
                cube = get_state_copy(init_state)  # vracamo

            max_y = min(y_from_moves) if len(
                y_from_moves) != 0 else (i % 32) * 0.03
            positions_x_reformed.append(np.array(cube))
            result_y.append(max_y)
            i += 1
            # print("current iter: " + str(i) +
            #       ", y value is: " + str(min(y_from_moves)))

        print("training epoche ")
        model.fit(np.asarray(positions_x_reformed, dtype=np.float32),
                  np.asarray(result_y, dtype=np.float32), batch_size=32, shuffle=False, epochs=100)

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
    learning(10000, 30, 1, model)

    # (10000 - random pozicija, za svaku generisati 12 sledecih poteza) * 30
    ##############################################################################

    # K - broj randomizovanja
    # k=1 - 12          -> 12, epoha=10000
    # k=2 - 244         ->
    # k=3 - 1728
    # k=4 - 20736
    # k=5 - 248832
    # k=6 - 2985984
    # k=7 - 35831808
    # k=8 - 429981696
