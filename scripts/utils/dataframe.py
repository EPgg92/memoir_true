#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utility function module to do operations on dataframes."""

from functools import reduce  # forward compatibility for Python 3
import operator
import pandas as pd
import numpy as np


def open_csv(path):
    """Return dataframe for a file encode with ISO-8859-1.

    :param path: path to a csv file.
    :type path: str
    :return: dataframe from the csv
    :rtype: pandas.core.frame.DataFrame
    """
    return pd.read_csv(path, encoding='utf-8')  # encoding='ISO-8859-1')


def _get_keyslist_of_recusive_dict(temp_dict, keys=[], list_of_keys=[]):
    for key in temp_dict:
        if type(temp_dict[key]) is dict:
            _get_keyslist_of_recusive_dict(
                temp_dict[key], keys + [key], list_of_keys)
        else:
            keys.append(key)
            list_of_keys.append(keys)
            keys = keys[:-1]
    return list_of_keys


def _get_values_of_recusive_dict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)


def transfrom_dictpath_into_dictdataframe(dict_of_path):
    """Transftorm a dict of paths into a dict of dataframes.

    The key of the output dict of dataframe is the join value by _ of all the
    list of keys recursif dict value.

    :param dict_of_path: recursif dict or not of paths
    :type df: dict(str)
    :return: simple dict of dataframes
    :rtype: dict(pandas.core.frame.DataFrame)
    """
    maps = _get_keyslist_of_recusive_dict(dict_of_path)
    return {"_".join(mapList): open_csv(_get_values_of_recusive_dict(
        dict_of_path, mapList)) for mapList in maps}


def suffle_dataframe(dataframe):
    return dataframe.sample(frac=1, random_state=42).reset_index(drop=True)


def combine_dataframe(list_of_dataframe):
    return pd.concat(list_of_dataframe).reset_index(drop=True)


def x_subdataframe(dataframe, x=4):
    return [pd.DataFrame(data=df).reset_index(drop=True)
            for df in np.array_split(dataframe, x)]


def save_dataframe(dataframe, path):
    dataframe.to_csv(path)


def get_prob_form_dataframe(dataframe, LABELS):
    return dataframe[LABELS].values
