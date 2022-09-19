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


def learning(model):
    states = []
    results = []

    for file_num in range(16):
        file = open('data/dataset_states_gen_100k_' + str(int(file_num)) + '.bin', 'rb')
        data = pickle.load(file)
        file.close()
        states.extend(data)

        result_y = [file_num+1] * len(data)
        results.extend(result_y)

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


def learning3(model, num_scrambles, num_states):  
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
    with open("models/model_rl5.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("models/model_rl5.json.h5")
    print("Saved model to disk")
    print('djura')


def learning4(model):  # B, K, M
    generate_dataset_2(16, 2560000)
    results = []

    file = open('data/dataset_states_gen_2_560_M.bin', 'rb')
    states = pickle.load(file)

    for i in range(16):
        results.extend([i+1] * int(2560000/16))

    model.fit(np.asarray(states, dtype=np.float32),
    np.asarray(results, dtype=np.float32), batch_size=1024, shuffle=True, epochs=150)

    model_json = model.to_json()
    with open("models/model_rl2.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("models/model_rl2.json.h5")
    print("Saved model to disk")
    print('djura')

def learningFinal(model):
    results = []

    file = open('data/dataset_states_gen_2_560_M.bin', 'rb')
    states = pickle.load(file)
    print(len(states))

    for i in range(20):
        results.extend([i+1] * int(200000/20))
    print(len(results))

    model.fit(np.asarray(states, dtype=np.float32),
    np.asarray(results, dtype=np.float32), batch_size=1024, shuffle=True, epochs=150)

    model_json = model.to_json()
    with open("models/model_sl_final.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("models/model_sl_final.json.h5")
    print("Saved model to disk")
    print('djura')


if __name__ == '__main__':
    generate_dataset_2(20, 200000) # 20000000
    model = create_NN()
    learningFinal(model)

    # json_file = open('models/model_rl.json', 'r')
    # loaded_model_json = json_file.read()
    # json_file.close()
    # loaded_model = model_from_json(loaded_model_json)
    # loaded_model.load_weights("models/model_rl.json.h5")
    # print("Loaded model from disk")

    # loaded_model.compile(loss="mean_squared_error", optimizer="adam")

    # learning4(loaded_model)


    # MORE TRAINING
    # for i in range(8):
    #     json_file = open('models/model_rl_final.json', 'r')
    #     loaded_model_json = json_file.read()
    #     json_file.close()
    #     loaded_model = model_from_json(loaded_model_json)
    #     loaded_model.load_weights("models/model_rl_final.json.h5")
    #     print("Loaded model from disk")

    #     loaded_model.compile(loss="mean_squared_error", optimizer="adam")

    #     learningFinal(loaded_model)
