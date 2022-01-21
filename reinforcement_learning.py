from scramble_cube import *
from neural_network import *


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
        positions_x = []
        for b in range(0, batch_size):  # ako je 32
            moves_for_gen = gen_random_moves(max_number_of_scrambles)
            cube = get_state_copy(finish_state)
            positions = []  # njih ce biti 25
            for m in moves_for_gen:
                rotate_cube(cube, m, moves.index(m[0]))
                # 24, 23, 22........... #1 - krajnje stanje
                positions.append(convert_to_np_array(cube))

            positions_x.extend(positions)

        result_y = []

        positions_x_reformed = []
        for x in positions_x:
            cube = get_state_copy(finish_state)
            convert_from_np_array(cube, x)
            init_state = get_state_copy(cube)
            y_from_moves = []
            for m in moves:
                rotate_cube(cube, m, moves.index(m[0]))
                if check_if_final(cube):
                    y_from_moves.append(0)
                    break
                else:
                    y = model.predict(convert_to_array_for_nn(cube))
                    y_from_moves.append(y)
                cube = get_state_copy(init_state)  # vracamo

            positions_x_reformed.append(convert_to_array_for_nn(cube))
            result_y.append(min(y_from_moves))

        # train_dataset = tf.data.Dataset.from_tensor_slices(
        #     (, result_y)).batch(32)
        print("training epoche ")
        model.fit(np.asarray(positions_x_reformed, dtype=np.float32),
                  np.asarray(result_y, dtype=np.float32), batch_size=32)

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
    learning(8, 32, 100, model)
