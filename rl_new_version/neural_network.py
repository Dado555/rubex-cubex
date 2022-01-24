import tensorflow as tf
import numpy as np
from tensorflow import *
from keras import *
from keras.layers import *
from keras.models import *
from keras_preprocessing import *
from tensorflow._api.v2 import data


def create_NN():
    model = Sequential()  # [Input(units=288, input_shape=[288], batch_size=1)]
    model.add(Dense(units=512, input_shape=(288,), activation="relu"))
    model.add(BatchNormalization())
    model.add(Dense(128, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dense(1, activation="relu"))

    model.summary()
    model.compile(loss="mean_squared_error", optimizer="adam")
    return model
