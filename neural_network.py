import numpy as np
import tensorflow as tf
from keras import *
from keras.layers import *
from keras.models import *
from keras_preprocessing import *
from tensorflow import *
from tensorflow._api.v2 import data


def create_NN():
    model = Sequential()  
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

    return model
