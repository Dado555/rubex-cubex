from generate_dataset import generate_dataset_2
from neural_network import *
import pickle
from scramble_cube import check_if_final, print_cube
import multiprocessing
import time


def populate_y(y_list, data, model):
    for i in range(len(data)):
        if check_if_final(data[i]):
            # j += 1
            y_list[i] = 0
        else:
            y_list[i] = abs(model(np.expand_dims(data[i], axis=0)))


def learning(model):  # B, K, M
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
    states = []
    results = []

    for file_num in range(16):
        file = open('data/dataset_states_gen_100k_' + str(int(file_num)) + '.bin', 'rb')
        data = pickle.load(file)
        file.close()
        states.extend(data)

        result_y = [file_num+1] * len(data)
        results.extend(result_y)
        # print(multiprocessing.cpu_count())
        # pool_obj = multiprocessing.Pool(multiprocessing.cpu_count())
        # pool_obj.map(populate_y(result_y, data, model), chunksize=int(len(data)/12)+1)
        # start = time.perf_counter()
        # p = multiprocessing.Process(target=populate_y, args=(result_y, data, model))
        # p.start()
        # p.join()
        # finish = time.perf_counter()
        # print('Finished in : ' + str(int(round(finish - start, 3))))

        # for i in range(len(data)):
        #     if check_if_final(data[i]):
        #         # j += 1
        #         result_y[i] = 0
        #     else:
        #         result_y[i] = abs(model(np.expand_dims(data[i], axis=0)))
        # finish = time.perf_counter()
        # print('Finished in : ' + str(int(round(finish - start, 3))))

    model.fit(np.asarray(states, dtype=np.float32),
    np.asarray(results, dtype=np.float32), batch_size=512, shuffle=True, epochs=150)

    model_json = model.to_json()
    with open("model_rl.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model_rl.json.h5")
    print("Saved model to disk")
    print('djura')


def learning2(model, num_scrambles, num_states):  # B, K, M
    states = []
    results = []

    file = open('data/dataset_states_gen_2M.bin', 'rb')
    states = pickle.load(file)
    print(len(states))
    print_cube(states[0])
    print_cube(states[80001])

    for i in range(25):
        results.extend([i+1] * int(num_states/num_scrambles))

    model.fit(np.asarray(states, dtype=np.float32),
    np.asarray(results, dtype=np.float32), batch_size=1024, shuffle=True, epochs=150)

    model_json = model.to_json()
    with open("model_rl5.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model_rl5.json.h5")
    print("Saved model to disk")
    print('djura')


def learning3(model, num_scrambles, num_states):  # B, K, M
    # generate_dataset_2()

    states = []
    results = []

    file = open('data/dataset_states_gen_2M.bin', 'rb')
    states = pickle.load(file)
    print(len(states))
    print_cube(states[0])
    print_cube(states[80001])

    for i in range(25):
        results.extend([i+1] * int(num_states/num_scrambles))

    model.fit(np.asarray(states, dtype=np.float32),
    np.asarray(results, dtype=np.float32), batch_size=1024, shuffle=True, epochs=150)

    model_json = model.to_json()
    with open("model_rl5.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model_rl5.json.h5")
    print("Saved model to disk")
    print('djura')


def learning4(model):  # B, K, M
    generate_dataset_2(16, 2560000)
    results = []

    file = open('data/dataset_states_gen_2_560_M.bin', 'rb')
    states = pickle.load(file)

    # for i in range(4):
    #     results.extend([i+1] * 10000)
    # results.extend([5] * 47002)
    # for i in range(6, 17):
    #     results.extend([i] * 224818)
    for i in range(16):
        results.extend([i+1] * int(2560000/16))

    model.fit(np.asarray(states, dtype=np.float32),
    np.asarray(results, dtype=np.float32), batch_size=1024, shuffle=True, epochs=150)

    model_json = model.to_json()
    with open("model_rl2.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model_rl2.json.h5")
    print("Saved model to disk")
    print('djura')


if __name__ == '__main__':
    # model = create_NN()
    # learning(model)

    json_file = open('model_rl.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model_rl.json.h5")
    print("Loaded model from disk")

    loaded_model.compile(loss="mean_squared_error", optimizer="adam")

    learning4(loaded_model)

    for i in range(8):
        json_file = open('model_rl2.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("model_rl2.json.h5")
        print("Loaded model from disk")

        loaded_model.compile(loss="mean_squared_error", optimizer="adam")

        learning4(loaded_model)
