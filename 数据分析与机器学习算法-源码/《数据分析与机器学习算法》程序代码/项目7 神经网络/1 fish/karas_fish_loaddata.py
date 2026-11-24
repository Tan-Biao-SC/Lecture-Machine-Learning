"""
karas_fish_loaddata.py
Created on Sat Aug 14 14:30:32 2021
author:
"""


import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from tensorflow.keras.optimizers import SGD

def data_pro():

    trainset = np.load("trainset.npy")
    evaluset = np.load("evaluset.npy")
    TL=trainset.shape[0]
    EL=evaluset.shape[0]
    tx = trainset[np.arange(TL), 0]
    ty = trainset[np.arange(TL), 1]
    evx = evaluset[np.arange(EL), 0]
    evy = evaluset[np.arange(EL), 1]

    return tx, ty, evx, evy

def model_train():
    tx, ty, evx, evy=data_pro()

    model = Sequential([
        Dense(2, input_dim=2,use_bias=True),
        Activation('softmax'),
    ])
    sgd=SGD(lr=0.002)
    model.compile(optimizer=sgd,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(tx, ty, epochs=10, batch_size=100)

    loss, accuracy = model.evaluate(evx, evy)

    print('test loss: ', loss)
    print('test accuracy: ', accuracy)

    print (model.weights)

if __name__ == "__main__":

    model_train()