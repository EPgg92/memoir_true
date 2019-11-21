import pandas as pd
import numpy as np
import itertools
from pprint import pprint
from collections import defaultdict as dd
from collections import Counter as cnt
from pprint import pprint
from keras.models import Sequential
from keras.layers import Dense, Activation
import keras
import tensorflow as tf


RELATED = ['agree', 'disagree', 'discuss']
LABEL = RELATED + ['unrelated']
DICT_LABELS = {lab: i for i, lab in enumerate(LABEL)}
REVERSED_DICT_LABELS = {i: lab for i, lab in enumerate(LABEL)}


def open_csv(file):
    return pd.read_csv(file, encoding='ISO-8859-1')


def get_list_dataframes(list_files, begin=0):
    return {file[begin:-4]: open_csv(file) for file in list_files}


def get_list_files(file_txt):
    return [f[:-1] for f in open(file_txt).readlines()]


def add_headline_to_csv(file):
    headline = "agree, disagree, discuss, unrelated\n"
    with open(file, 'r') as data:
        data = data.read()
    with open(file, 'w+') as to_write:
        to_write.write(headline + data)
    # [add_headline_to_csv(file) for file in list_files_probs]


def combine_labels(ll):
    dataframe = pd.DataFrame()
    for key in ll:
        dataframe[key] = ll[key]['Stance'].tolist()
    return dataframe


def majortity_vote(all_combined_label, models=['1', '2', '3', '4']):
    priority = {'agree': 0.1, 'disagree': 0.0,
                'discuss': 0.2, 'unrelated': 0.3}
    vote = []
    for line in all_combined_label[models].values.tolist():
        cnt_line = cnt(line)
        dict_line = {cnt_line[key] + priority[key]: key for key in cnt_line}
        vote.append(dict_line[max(dict_line.keys())])
    return vote


def create_vecs(lp):
    dataframe = pd.DataFrame()
    for key in lp:
        for lab in lp[key]:
            dataframe[lab + key] = lp[key][lab].tolist()
    return dataframe.as_matrix()


def get_list_labels(file):
    return open_csv(file)["Stance"].as_matrix()


def create_trained_nn(vecs_train, labels_train, epochs=50):
    """Create a trained neural network model."""
    input_dim = vecs_train.shape[1]
    model = Sequential()
    model.add(Dense(units=100, input_dim=input_dim))
    model.add(Activation('relu'))
    model.add(Dense(units=4))
    model.add(Activation('softmax'))
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='sgd',
                  metrics=['accuracy'])
    model.fit(vecs_train, labels_train, epochs=epochs, batch_size=32)

    return model


def predict_nn(model, vecs_test, labels_test):
    """Permit to do prediction with neural network model."""
    return [(pred, label) for pred, label in zip(
        model.predict_classes(vecs_test), labels_test)]


def main():
    pass


if __name__ == '__main__':
    list_files_probs = get_list_files('files_probs.txt')
    list_df_probs = get_list_dataframes(list_files_probs, 31)
    list_files_label = get_list_files('files_labels.txt')
    list_df_label = get_list_dataframes(list_files_label, 25)
    all_combined_label = combine_labels(list_df_label)
    vecs_train = create_vecs(list_df_probs)
    labels_train = get_list_labels('dev_test.csv')
    print(labels_train)
