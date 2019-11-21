#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Docstring.'''


import utils.stack as st
import utils.dataframe as df
import utils.file as fl
import utils.datasets as ds
import numpy as np
import pandas as pd


def main():
    labels_number = fl.open_yml('../config/constants.yml')['labels_number']
    path_solat = '../datasets/ensemble_learning/results/solat/_{}.csv'
    path_uclmr = '../datasets/ensemble_learning/results/uclmr/_{}.csv'
    path_labels = '../datasets/ensemble_learning/_10/subtrain{}/test.csv'
    path_test_labels = '../datasets/competition_test/' + \
        'competition_test_stances.csv'

    solat = [df.open_csv(path_solat.format(x)).as_matrix(
        ['prob_0', 'prob_1', 'prob_2', 'prob_3']) for x in range(10)]
    uclmr = [st.get_stack_form_csv(path_uclmr.format(x)) for x in range(10)]

    train_vectors = st.lign_align(
        [st.column_align(solat), st.column_align(uclmr)])
    train_labels = [df.open_csv(path_labels.format(x)).as_matrix(
        ['Stance']) for x in range(10)]
    train_labels = st.column_align(train_labels)
    train_labels = [labels_number[lab[0]] for lab in train_labels]

    test_solat = df.open_csv(path_solat.format('test')).as_matrix(
        ['prob_0', 'prob_1', 'prob_2', 'prob_3'])
    test_uclmr = st.get_stack_form_csv(path_uclmr.format('test'))

    test_vectors = st.lign_align([test_solat, test_uclmr])
    test_labels = [labels_number[lab]
                   for lab in df.open_csv(path_test_labels)['Stance'].values]

    tag_vec = ['solat_agree', 'solat_disagree', 'solat_discuss',
               'solat_unrelated', 'uclmr_agree', 'uclmr_disagree',
               'uclmr_discuss', 'uclmr_unrelated', ]
    tag_lab = ['Stance']

    train_vectors = pd.DataFrame(data=train_vectors, columns=tag_vec)
    train_labels = pd.DataFrame(data=train_labels, columns=tag_lab)
    test_vectors = pd.DataFrame(data=test_vectors, columns=tag_vec)
    test_labels = pd.DataFrame(data=test_labels, columns=tag_lab)

    dev_train_vectors, dev_test_vectors = ds.create_first_analyse_datasets(
        train_vectors, cols=tag_vec)

    dev_train_labels, dev_test_labels = ds.create_first_analyse_datasets(
        train_labels, cols=tag_lab)

    train_vectors.to_csv('vectors/train_vectors.csv')
    train_labels.to_csv('vectors/train_labels.csv')
    test_vectors.to_csv('vectors/test_vectors.csv')
    test_labels.to_csv('vectors/test_labels.csv')
    dev_train_vectors.to_csv('vectors/dev_train_vectors.csv')
    dev_test_vectors.to_csv('vectors/dev_test_vectors.csv')
    dev_train_labels.to_csv('vectors/dev_train_labels.csv')
    dev_test_labels.to_csv('vectors/dev_test_labels.csv')


if __name__ == '__main__':
    main()
