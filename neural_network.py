import numpy as np
import tensorflow as tf
from keras import *
from keras.layers import *
from keras.models import *
from keras_preprocessing import *
from tensorflow import *
from tensorflow._api.v2 import data


def create_NN():
    model = Sequential()  # [Input(units=288, input_shape=[288], batch_size=1)]
    model.add(Dense(units=1024, input_shape=(288,), activation="relu"))
    model.add(BatchNormalization())
    model.add(Dense(512, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dense(512, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dense(256, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dense(128, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dense(1, activation="relu"))

    model.summary()
    model.compile(loss="mean_squared_error", optimizer="adam")
    # input = Input(shape=(288,))
    # layer_1 = Dense(1024, activation="relu")(input)
    # layer_2 = Dense(512, activation="relu")(layer_1)
    # layer_3 = Dense(256, activation="relu")(layer_2)
    # output = Dense(1, activation="relu")(layer_3)

    # model = Model(input, output)
    # model.summary()
    # model.compile(loss="mean_squared_error", optimizer="adam")

    return model
