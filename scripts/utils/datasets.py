#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Docstring."""

import utils.dataframe as df
import os
ROOT_ENSEMBLE_LEARNING = '../datasets/ensemble_learning/'


def _select_on_mod5(dataframe, cols):
    """Return 20 percent of the input dataframe on selected colums.

    Using modulo 5 to do the job.

    :param dataframe: dataframe which have a col id
    :type dataframe: pandas.core.frame.DataFrame
    :param cols: list of colums wished default only Stance col
    :type path: list
    :return: 20 percent of the input dataframe on selected colums
    :rtype: pandas.core.frame.DataFrame
    """
    return dataframe.loc[(dataframe['id']) % 5 == 0][cols].reset_index(drop=True)


def _select_on_not_mod5(dataframe, cols):
    """Return 80 percent of the input dataframe on selected colums.

    Using modulo 5 to do the job.

    :param dataframe: dataframe which have a col id
    :type dataframe: pandas.core.frame.DataFrame
    :param cols: list of colums wished default only Stance col
    :type path: list
    :return: 80 percent of the input dataframe on selected colums
    :rtype: pandas.core.frame.DataFrame
    """
    return dataframe.loc[(dataframe['id']) % 5 != 0][cols].reset_index(drop=True)


def create_first_analyse_datasets(dataframe, cols=['Stance']):
    """Return the dev set and train set in a list.

    :param dataframe: dataframe which have a col id
    :type dataframe: pandas.core.frame.DataFrame
    :param cols: list of colums wished default only Stance col
    :type path: list
    :return: list of two element [first is dev set, second train set]
    :rtype: list
    """
    dataframe['id'] = [x for x in range(dataframe.shape[0])]
    mod5 = _select_on_mod5(dataframe, cols)
    not_mod5 = _select_on_not_mod5(
        dataframe, cols)
    return mod5, not_mod5


def create_train_datasets_ssl(dataframe, nb_subdataframe):
    subdataframe = df.x_subdataframe(dataframe, nb_subdataframe)
    list_couple_train_test_subtrain = []
    for i, dataframe in enumerate(subdataframe):
        copy_subdataframe = subdataframe.copy()
        test = copy_subdataframe.pop(i).reset_index(drop=True)
        train = df.combine_dataframe(copy_subdataframe)
        list_couple_train_test_subtrain.append((test, train))
    return list_couple_train_test_subtrain


def save_list_couple_tt_subtrain(list_couple_train_test_subtrain, updir=""):
    updir = updir + '/'
    for i, tt in enumerate(list_couple_train_test_subtrain):
        test, train = tt
        directory = "{}{}{}{}".format(
            ROOT_ENSEMBLE_LEARNING, updir, "subtrain", i)
        if not os.path.exists(directory):
            os.makedirs(directory)
        df.save_dataframe(test, "{}/test.csv".format(directory))
        df.save_dataframe(train, "{}/train.csv".format(directory))
