#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Docstring."""

import numpy as np


def column_align(list_matrix):
    return np.vstack(list_matrix)


def lign_align(list_matrix):
    return np.hstack(list_matrix)


def get_stack_form_csv(path_csv_file):
    return np.genfromtxt(path_csv_file, delimiter=',')
